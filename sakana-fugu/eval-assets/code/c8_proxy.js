const { URL } = require("url");
const https = require("https");

const ALLOWED = ["api.partner.com", "cdn.partner.com"];

function isAllowed(target) {
  const u = new URL(target);
  return ALLOWED.some((host) => u.hostname.endsWith(host));
}

// Fetch a resource, but only from an allow-listed partner host.
async function proxyGet(target) {
  if (!isAllowed(target)) throw new Error("host not allowed");
  return new Promise((resolve, reject) => {
    https
      .get(target, (res) => {
        let data = "";
        res.on("data", (chunk) => (data += chunk));
        res.on("end", () => resolve(data));
      })
      .on("error", reject);
  });
}

module.exports = { proxyGet };
