window = global
function v(t) {
    t = window.encodeURIComponent(t).replace(/%([0-9A-F]{2})/g, function(n, t) {
        return o("0x" + t)
    });
        return window.btoa(t)

}
var f2 = "66",
    s2 = "72",
    d2 = "6f",
    m2 = "6d",
    l2 = "43",
    v2 = "68",
    p2 = "61",
    h2 = "64",
    y2 = "65",
    g2 = "unescape",
    w2 = "%u00",
    b2 = "String",
    _ = "";

function o(n) {
    return String.fromCharCode(n)
    // t = _,
    // [f2, s2, d2, m2, l2, v2, p2, s2, l2, d2, h2, y2].forEach(function(n) {
    //     t += window.unescape(w2 + n)
    // });
    // var t, e = t;
    // console.log(window.String())
    // return window.String([e](n))
}
function h(n, t) {

    R = "length";
    q1 = "charCodeAt";
    H = 0;
    for (var e = (n = n.split('')).length, r = t.toString().length, a = q1, i = H; i < e; i++)
        n[i] = o(n[i].charCodeAt(H) ^ t[(i + 10) % r].charCodeAt(H));
    return n.join(_)
}


function url(ti, a){
    var shjian = ti -1 - 1661224081041
    a = v(a)+"@#/rank/indexPlus/brand_id/2@#"+shjian+"@#3"
    e = (0, v)((0, h)(a, "xyz517cda96abcd"))
    console.log(e)
    return e;
}
