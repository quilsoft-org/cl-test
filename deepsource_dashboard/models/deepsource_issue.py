from odoo import models, fields, api
import requests
from datetime import date

class DeepSourceIssue(models.Model):
    _name = "deepsource.issue"
    _description = "DeepSource Issue"

    title = fields.Char()
    issue_code = fields.Char()
    severity = fields.Char()
    category = fields.Char()
    link = fields.Char()
    fetched_date = fields.Date(default=lambda self: date.today())


class DeepSourceStat(models.Model):
    _name = "deepsource.stat"
    _description = "DeepSource Sync Stats"
    _order = "date desc"

    date = fields.Date()
    critical = fields.Integer()
    major = fields.Integer()
    minor = fields.Integer()


class DeepSourceSync(models.TransientModel):
    _name = "deepsource.sync"
    _description = "Sync DeepSource Issues"

    @api.model
    def sync_issues(self):


        import wdb;wdb.set_trace()

        IrConfig = self.env['ir.config_parameter'].sudo()
        token = IrConfig.get_param('deepsource.token')
        repo_name = IrConfig.get_param('deepsource.repo')
        org = "quilsoft-org"

        if not token or not repo_name:
            return

        query = """
            query ($owner: String!, $name: String!) {
              repository(
                platform: GITHUB
                owner: $owner
                name: $name
              ) {
                issues(first: 200, states: [OPEN]) {
                  edges {
                    node {
                      title
                      issueCode
                      severity
                      category
                      permalink
                    }
                  }
                }
              }
            }
        """

        variables = {
            "owner": "quilsoft-org",
            "name": repo_name
        }

        response = requests.post(
            "https://api.deepsource.io/graphql",
            json={"query": query, "variables": variables},
            headers={"Authorization": f"Bearer {token}"}
        )
        data = response.json()
        edges = data.get("data", {}).get("repository", {}).get("issues", {}).get("edges", [])

        self.env["deepsource.issue"].search([]).unlink()

        severities = {"critical": 0, "major": 0, "minor": 0}

        for edge in edges:
            node = edge["node"]
            sev = node["severity"].lower()
            if sev in severities:
                severities[sev] += 1

            self.env["deepsource.issue"].create({
                "title": node["title"],
                "issue_code": node["issueCode"],
                "severity": node["severity"],
                "category": node["category"],
                "link": node["permalink"],
            })

        self.env["deepsource.stat"].create({
            "date": date.today(),
            "critical": severities["critical"],
            "major": severities["major"],
            "minor": severities["minor"],
        })
