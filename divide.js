// divide.js
function divide(a, b) {
  const x = Number(a);
  const y = Number(b);
  if (!isFinite(x) || !isFinite(y)) {
    throw new TypeError('Arguments must be finite numbers');
  }
  if (y === 0) {
    throw new Error('Division by zero');
  }
  return x / y;
}

if (require.main === module) {
  const [,, a, b] = process.argv;
  if (a === undefined || b === undefined) {
    console.log('Usage: node divide.js <a> <b>');
    process.exit(2);
  }
  try {
    console.log(divide(a, b));
  } catch (e) {
    console.error(e.message);
    process.exit(1);
  }
}

module.exports = { divide };
