const https = require('https');
https.get('https://www.dealtoday.vn/', (res) => {
    let d = '';
    res.on('data', c => d += c);
    res.on('end', () => {
        const matches = d.match(/src="([^"]+\.(png|jpg|jpeg|webp))"/gi) || [];
        const unique = [...new Set(matches.map(s => s.replace('src="', '').replace('"', '')))].filter(s => s.includes('http'));
        console.log(JSON.stringify(unique.slice(0, 20), null, 2));
    });
});
