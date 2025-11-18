const fs = require("fs");
const path = require("path");

const distDir = path.resolve(__dirname, "../web_dist");
const qrcPath = path.resolve(__dirname, "../web_dist/web_view.qrc");

// recursively collect all files
function collectFiles(dir) {
  let files = [];
  for (const item of fs.readdirSync(dir)) {
    const fp = path.join(dir, item);
    const stat = fs.statSync(fp);
    if (stat.isDirectory()) {
      files = files.concat(collectFiles(fp));
    } else {
      files.push(fp);
    }
  }
  return files;
}

const files = collectFiles(distDir);

// convert to paths relative to resources/
function qrcPathOf(file) {
  const rel = path.relative(path.resolve(__dirname, "../web_dist"), file);
  return rel.replace(/\\/g, "/");
}

const xml =
  `<RCC>\n  <qresource prefix="/web_view">\n` +
  files
    .map((f) => `    <file>${qrcPathOf(f)}</file>`)
    .join("\n") +
  `\n  </qresource>\n</RCC>\n`;

fs.writeFileSync(qrcPath, xml, "utf8");

console.log("Generated:", qrcPath);
