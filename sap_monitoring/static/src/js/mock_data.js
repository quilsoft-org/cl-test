/** @odoo-module **/
// Simple mock time series generator
export function generateMockSeries(startDate, endDate, min=10, max=200, intervalMinutes=60){
    const start = new Date(startDate);
    const end = new Date(endDate);
    const labels = [];
    const values = [];
    const diffMs = end - start;
    const totalMinutes = Math.max(1, Math.floor(diffMs / 60000));
    // compute step to have around ~100 points max
    const approxPoints = 100;
    const step = Math.max(1, Math.floor(totalMinutes / approxPoints));
    const stepMs = step * 60 * 1000;
    for (let t = start.getTime(); t <= end.getTime(); t += stepMs) {
        const d = new Date(t);
        const hh = d.getHours().toString().padStart(2,'0');
        const mm = d.getMinutes().toString().padStart(2,'0');
        const label = `${d.getFullYear()}-${(d.getMonth()+1).toString().padStart(2,'0')}-${d.getDate().toString().padStart(2,'0')} ${hh}:${mm}`;
        labels.push(label);
        // pseudo-random value with some sinusoidal variation
        const base = min + Math.random() * (max - min);
        const seasonal = Math.round((Math.sin(t/ (1000*60*60*6)) + 1) * 0.5 * (max-min)/4);
        const value = Math.max(0, Math.round(base + seasonal));
        values.push(value);
    }
    return { labels, values };
}
