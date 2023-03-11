API_KEY = "a2c903cc-b31e-4547-9299-b6d07b7631ab"
window = global
function encryptApiKey() {
    var t = API_KEY
      , e = t.split("")
      , r = e.splice(0, 8);
    // -b31e-4547-9299-b6d07b7631aba2c903cc
    return e.concat(r).join("")
}
function encryptTime(t) {
    var e = (1 * t + 1111111111111).toString().split("")
      , r = parseInt(10 * Math.random(), 10)
      , n = parseInt(10 * Math.random(), 10)
      , o = parseInt(10 * Math.random(), 10);
    return e.concat([r, n, o]).join("")
}
function comb(t, e) {
    var r = "".concat(t, "|").concat(e);
    console.log(r)
    return window.btoa(r)
}

function getApiKey(t) {
    var e = encryptApiKey();
    return t = encryptTime(t),
    comb(e, t)
}

console.log(getApiKey((new Date()).getTime()))