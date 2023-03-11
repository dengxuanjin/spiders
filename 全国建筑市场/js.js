
var n = Object.create || function() {
                    function e() {}
                    return function(t) {
                        var n;
                        return e.prototype = t,
                        n = new e,
                        e.prototype = null,
                        n
                    }
                }()

var t;
o  = function() {
                    return {
                        extend: function(e) {
                            t = n(this);
                            return e && t.mixIn(e),
                            t.hasOwnProperty("init") && this.init !== t.init || (t.init = function() {
                                t.$super.init.apply(this, arguments)
                            }
                            ),
                            t.init.prototype = t,
                            t.$super = this,
                            t
                        },
                        create: function() {
                            var e = this.extend();
                            return e.init.apply(e, arguments),
                            e
                        },
                        init: function() {},
                        mixIn: function(e) {
                            for (var t in e)
                                e.hasOwnProperty(t) && (this[t] = e[t]);
                            e.hasOwnProperty("toString") && (this.toString = e.toString)
                        },
                        clone: function() {
                            return this.init.prototype.extend(this)
                        }
                    }
                }()
s = o.extend({
                    init: function(e, n) {
                        e = this.words = e || [],
                        this.sigBytes = n !== t ? n : 4 * e.length
                    },
                    toString: function(e) {
                        return (e || l).stringify(this)
                    },
                    concat: function(e) {
                        var t = this.words
                          , n = e.words
                          , i = this.sigBytes
                          , r = e.sigBytes;
                        if (this.clamp(),
                        i % 4)
                            for (var o = 0; o < r; o++) {
                                var s = n[o >>> 2] >>> 24 - o % 4 * 8 & 255;
                                t[i + o >>> 2] |= s << 24 - (i + o) % 4 * 8
                            }
                        else
                            for (o = 0; o < r; o += 4)
                                t[i + o >>> 2] = n[o >>> 2];
                        return this.sigBytes += r,
                        this
                    },
                    clamp: function() {
                        var t = this.words
                          , n = this.sigBytes;
                        t[n >>> 2] &= 4294967295 << 32 - n % 4 * 8,
                        t.length = Math.ceil(n / 4)
                    },
                    clone: function() {
                        var e = o.clone.call(this);
                        return e.words = this.words.slice(0),
                        e
                    },
                    random: function(t) {
                        for (var n, i = [], r = function(t) {
                            t = t;
                            var n = 987654321
                              , i = 4294967295;
                            return function() {
                                n = 36969 * (65535 & n) + (n >> 16) & i,
                                t = 18e3 * (65535 & t) + (t >> 16) & i;
                                var r = (n << 16) + t & i;
                                return r /= 4294967296,
                                r += .5,
                                r * (e.random() > .5 ? 1 : -1)
                            }
                        }, o = 0; o < t; o += 4) {
                            var a = r(4294967296 * (n || e.random()));
                            n = 987654071 * a(),
                            i.push(4294967296 * a() | 0)
                        }
                        return new s.init(i,t)
                    }
                })
function parse(e) {
                        for (var t = e.length, n = [], i = 0; i < t; i += 2)
                            n[i >>> 3] |= parseInt(e.substr(i, 2), 16) << 24 - i % 8 * 4;
                        return new s.init(n,t / 2)
                    }
c = {
                    stringify: function(e) {
                        for (var t = e.words, n = e.sigBytes, i = [], r = 0; r < n; r++) {
                            var o = t[r >>> 2] >>> 24 - r % 4 * 8 & 255;
                            i.push(String.fromCharCode(o))
                        }
                        return i.join("")
                    },
                    parse: function(e) {
                        for (var t = e.length, n = [], i = 0; i < t; i++)
                            n[i >>> 2] |= (255 & e.charCodeAt(i)) << 24 - i % 4 * 8;
                        return new s.init(n,t)
                    }
                }

Base64 = {
    stringify: function(e) {
        var t = e.words
          , n = e.sigBytes
          , i = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=';
        e.clamp();
        for (var r = [], o = 0; o < n; o += 3)
            for (var s = t[o >>> 2] >>> 24 - o % 4 * 8 & 255, a = t[o + 1 >>> 2] >>> 24 - (o + 1) % 4 * 8 & 255, l = t[o + 2 >>> 2] >>> 24 - (o + 2) % 4 * 8 & 255, c = s << 16 | a << 8 | l, u = 0; u < 4 && o + .75 * u < n; u++)
                r.push(i.charAt(c >>> 6 * (3 - u) & 63));
        var h = i.charAt(64);
        if (h)
            while (r.length % 4)
                r.push(h);
        return r.join("")
    }}

Utf8 = {
        stringify: function(e) {
            try {
                return decodeURIComponent(escape(c.stringify(e)))
            } catch (t) {
                throw new Error("Malformed UTF-8 data")
            }
        },
        parse: function(e) {
            return c.parse(unescape(encodeURIComponent(e)))
        }
    }

Pkcs7 = {
    pad: function(e, t) {
        for (var n = 4 * t, i = n - e.sigBytes % n, r = i << 24 | i << 16 | i << 8 | i, s = [], a = 0; a < i; a += 4)
            s.push(r);
        var l = o.create(s, i);
        e.concat(l)
    },
    unpad: function(e) {
        var t = 255 & e.words[e.sigBytes - 1 >>> 2];
        e.sigBytes -= t
    }
}
CBC = function() {
    var e = f.extend();
    function n(e, n, i) {
        var r = this._iv;
        if (r) {
            var o = r;
            this._iv = t
        } else
            o = this._prevBlock;
        for (var s = 0; s < i; s++)
            e[n + s] ^= o[s]
    }
    return e.Encryptor = e.extend({
        processBlock: function(e, t) {
            var i = this._cipher
              , r = i.blockSize;
            n.call(this, e, t, r),
            i.encryptBlock(e, t),
            this._prevBlock = e.slice(t, t + r)
        }
    }),
    e.Decryptor = e.extend({
        processBlock: function(e, t) {
            var i = this._cipher
              , r = i.blockSize
              , o = e.slice(t, t + r);
            i.decryptBlock(e, t),
            n.call(this, e, t, r),
            this._prevBlock = o
        }
    }),
    e
}
l = Utf8
m = Utf8.parse("0123456789ABCDEF")
h =s.extend({
    cfg: o.extend(),
    createEncryptor: function(e, t) {
        return this.create(this._ENC_XFORM_MODE, e, t)
    },
    createDecryptor: function(e, t) {
        return this.create(this._DEC_XFORM_MODE, e, t)
    },
    init: function(e, t, n) {
        this.cfg = this.cfg.extend(n),
        this._xformMode = e,
        this._key = t,
        this.reset()
    },
    reset: function() {
        s.reset.call(this),
        this._doReset()
    },
    process: function(e) {
        return this._append(e),
        this._process()
    },
    finalize: function(e) {
        e && this._append(e);
        var t = this._doFinalize();
        return t
    },
    keySize: 4,
    ivSize: 4,
    _ENC_XFORM_MODE: 1,
    _DEC_XFORM_MODE: 2,
    _createHelper: function() {
        function e(e) {
            return "string" == typeof e ? C : _
        }
        return function(t) {
            return {
                encrypt: function(n, i, r) {
                    return e(i).encrypt(t, n, i, r)
                },
                decrypt: function(n, i, r) {
                    return e(i).decrypt(t, n, i, r)
                }
            }
        }
    }()
})
g = (h.extend({
    cfg: h.cfg.extend({
        mode: CBC,
        padding: Pkcs7
    }),
    reset: function() {
        h.reset.call(this);
        var e = this.cfg
          , t = e.iv
          , n = e.mode;
        if (this._xformMode == this._ENC_XFORM_MODE)
            var i = n.createEncryptor;
        else {
            i = n.createDecryptor;
            this._minBufferSize = 1
        }
        this._mode && this._mode.__creator == i ? this._mode.init(this, t && t.words) : (this._mode = i.call(n, this, t && t.words),
        this._mode.__creator = i)
    },
    _doProcessBlock: function(e, t) {
        this._mode.processBlock(e, t)
    },
    _doFinalize: function() {
        var e = this.cfg.padding;
        if (this._xformMode == this._ENC_XFORM_MODE) {
            e.pad(this._data, this.blockSize);
            var t = this._process(!0)
        } else {
            t = this._process(!0);
            e.unpad(t)
        }
        return t
    },
    blockSize: 4
}),
n.CipherParams = m.extend({
    init: function(e) {
        this.mixIn(e)
    },
    toString: function(e) {
        return (e || this.formatter).stringify(this)
    }
}))
 f = m.extend({
    createEncryptor: function(e, t) {
        return this.Encryptor.create(e, t)
    },
    createDecryptor: function(e, t) {
        return o.create(e, t)
    },
    init: function(e, t) {
        this._cipher = e,
        this._iv = t
    }
})
y = {
    stringify: function(e) {
        var t = e.ciphertext
          , n = e.salt;
        if (n)
            var i = o.create([1398893684, 1701076831]).concat(n).concat(t);
        else
            i = t;
        return i.toString(l)
    },
    parse: function(e) {
        var t = l.parse(e)
          , n = t.words;
        if (1398893684 == n[0] && 1701076831 == n[1]) {
            var i = o.create(n.slice(2, 4));
            n.splice(0, 4),
            t.sigBytes -= 16
        }
        return g.create({
            ciphertext: t,
            salt: i
        })
    }
    }


_ = m.extend({
    cfg: m.extend({
    format: y
    }),
    encrypt: function(e, t, n, i) {
        i = this.cfg.extend(i);
        var r = e.createEncryptor(n, i)
          , o = r.finalize(t)
          , s = r.cfg;
        return g.create({
            ciphertext: o,
            key: n,
            iv: s.iv,
            algorithm: e,
            mode: s.mode,
            padding: s.padding,
            blockSize: e.blockSize,
            formatter: i.format
        })
    },
    decrypt: function(e, t, n, i) {
        var e = f.extend();
        i = this.cfg.extend(i),
        t = this._parse(t, i.format);
        var r = e.createDecryptor(n, i);
        return r
    },
    _parse: function(e, t) {
        return "string" == typeof e ? t.parse(e, this) : e
    }
})

C = _.extend({
                    encrypt: function(e, t, n, i) {
                        i = this.cfg.extend(i);
                        var r = i.kdf.execute(n, e.keySize, e.ivSize);
                        i.iv = r.iv;
                        var o = _.encrypt.call(this, e, t, r.key, i);
                        return o.mixIn(r),
                        o
                    },
                    decrypt: function(e, t, n, i) {
                        i = this.cfg.extend(i),
                        t = this._parse(t, i.format);
                        var r = i.kdf.execute(n, e.keySize, e.ivSize, t.salt);
                        i.iv = r.iv;
                        var o = _.decrypt.call(this, e, t, r.key, i);
                        return o
                    }
                })
function k(e){
    return "string" == typeof e ? C : _;
}
function decrypt(n, i, r) {
        return k(i).decrypt(t, n, i, r)
    }

function sb(t) {
    var e = parse(t),
    f = Utf8.parse("jo8j9wGw%6HbxfFn"),
    m = Utf8.parse("0123456789ABCDEF"),
    n = Base64.stringify(e),
    a = decrypt(n, f, {
    iv: m,
    mode: CBC,
    padding: Pkcs7
})
    // console.log(CBC)
    // r = e.toString(Utf8.parse());
    console.log()
    // return r.toString()
}
let data = '95780ba0943730051dccb5fe3918f9fe1b6f2130681f99d5620c5497aa480f13f32e8cc4b2f871a9a59a1d0117ce9456ce6b66396085eaa2822aa2ffc121eac1885d297bbd68dcda88cd8b0b29e282f9fd6b8392d52b817608665d8a565119f3346fb19449490842b923ec5781524595bc078b2c15e47473f15860e2ed45c9dbab5a750581a26fcb22b99228eb09b541e83ac3724f373a7512ac3827fa40354d1e9af350488194daf6b0317870a9a65dee320e0d4cb84708b25e383c02095c17f20d09fb39ab6e1a150c85818ecc2a31c384412859eff0026319094965cffffbc42c9495ee35f03b2440b8baac751927c38b616dc2042a64223fa6a72f1dc685fcbb38fd7cc47f1efbc9f5bd2c7490e58fbd36cf5a3b4be852fac87c6e682bb7d554b9990431e2d550d914754c6ac899fef97980084a6ba4bfda771be81ea11fd1542b6ffafe1439be2c94f74f6a83bfce6d2bc2e9dc1d86b84eeb85c2b8dda8846d65232148f9d88ac4a675d2049c1ac6efae1e4a5f4a106f0e627fb89199d9491303a792672832269e9a5cc208be00fbf1baf342262ebdbef5eaf3a50a52eeae2811f2813697018bf103df428dc0d496af435d2384b2198000add245d87233c3955695a6daa1bb4bc5a8657b2c9dfbf9f4067097df759f5724a5cb3a747a58509e2f22da6cbcdd29ba95dc555cd40cba6d0a2eced0b15ece067bc949dce784b2ceb06a61e9f7dc8943445da701c15fc7053f2c21ea1fc877e02280d22f913983c6f1dead091312c37aa90a5967b71b4c34dab24468bde5f747d8f44f8fd4b0fa493ff49b92441a7e1e8c256a6a18573baa1bf16f5093e36a7c9e282a3156dba776ea6a94794c9a034ae4f5e77761e49569d194d10703302476e7fd8e25ab4669f0c7a6c7d0e2680847d77ea5a585f7f60e7fcebb1ae791b8216bb25b644f5094157bd62c6aebf0a7faf173b2fde0da6f9ebb0dcab8a129c11b9f972445aee5297d38e0cc72d0b4d9c84c7e6b0ecf592d37998d04df8c52d5776c2741863b5fefd69302f176909b6bc065c4b81fc959a348368d250a03a86145f81950937ca83e3a765e6afd71d00c68faeca8d4d76f5ad762fc7d17fd05894857841bec355bb1d7f75db95c8e30dea58536ac6288fd3429ca9ab48d1eddb48631734ce2a574d79b93952fa2c9e9665c6337b35ea2309344cd22fe1b92dbd02051917d6c5edf1f2259c5f8a0cb3fbd00391c298f0461ba16a2300337d0b60b224bc6b796cedeb427cd07d97f17460d490bc3b112d2b8403026ff5ff5a70dde82cf210f22c3c206ca3bfe34cc137bedad0f1ae712d7168226a42fd22f9e17dede40654157e4c4756bd10292c7d0e2eefba36634309aeb24d3725802243e2003a68dac0a3b539eed0dca51f6f0d57a5c58a117fc56910d0e7319b05e0fc4a5137952e2f958636b584973da7dd61b63101e2d0cffe2b249c562b72b64fb6ca67ed0246bf0f9185fe22c87dc6d3c8374239dd4e70cdbc5ccacbd359dea203c021ac7d54998b2f1571d7f787a3ce1c4fda45037bd33be1ff9da883a556e2ef81ad2047d35a5065e73402e0e02231bcb3724445df198ad53112db4690091a98edea0fd194480b4193c2e9bb1cee1fb37654fce593cc88c59537003dd297be5d88834ec00595a4dda9fe44e14193482f1d212cf33ec58be3edfbecf7c7908bbf4c4b9beee5d0ef148e1bbdae9daea30beadcc6f5639a6f4eb57719fda5bc0e8766a52da34f17f2aa1a4b608fb6e53938d8e74d3b53aaeee663e1053e8444d44fb7a782d3b087155c9341559ada772299b988e859039435751592c25532090c0cc1a4445ba93ab3a1c9e8cd198251ed3ed76cc5091b83ead3cf1e11ceeeb0461e923c394a0a9f37220b9a5ed8e5f01b360eb6661a6456cde6a4497186567d4324d469277be217c03b84048ad272a3ea49b943f4c7c70487d060cd24cd9ea61032207c2a13c1384e0b5159d70d78d5e224401b5142ca2548ff2a13d1029a3b54dd68c7ac03d2c004c645ea586cdebf96267fffac4079305e37ab11e3af6bdff0e296ee4b5efdd00b48f44a91eb8475ddd6668a0b7548a7640229aeb650f76e02005b782a0a082175f256654aa8e0f3e3675726c9697978fd4ac35b6b64107e373cf80a9881152e62b2c1841292dbc40c41a7a36c8d353f2add2731415dcd81be8b3cdbfe26dec973a4e6edf2382992409db93aea8f354fbea21a21c54747ac540e752b5b13fee5f5d30277de7178eb998e31656b266c4de884a878251d6108ef36bfe8ec1020cbd469debe57478fb3af6d369a6e12499ba5ee436cef3f3089aa1710a0ddf84809875b5fb0cf1ee1aedbb25e0df0617f1ec2b6bea1671d2adf79a7d6789b019218bcc7219cb9a53f47dcffccd129a48cebb2433fa9d7e547a651a09c2bf4637639d2c08aee3d7e10d2b2474e1a4ecc22e932cddfd6c4caa781af8eed3a8ff0a261ae116e1c0243d3a9f5a719589b74cedef35211e8418666773b5609cb15c31bf853c7251de71deecbc162422004e1598fc302636cddd8d32ccb6b02ff634a998dfd9c9eaee59dc6b1bb5391ed7e38a8cb1154f4ff99c8b8c4c75c376d9682014020a45b27bce28e5557764268bbf17eda386848c6cb21e2ddb909ac4f70fd740f630827b40f54cc6465070c332910373992fe2caefbc3b189f9ad31bc224625ddeac99320844bd4db8cbc265b8d5f4609b97ae76d504a4dd553a87586058dbcb7b08128339c2f3ec4f4bd8d34e7d5cacc01239361e005a56e2ca47449cb7df91b64190b36b267954be47177df4e4b29e56ded5f9e59fe914d650f81bc44c4ac3eda44cbf6d793b64fbba7358ebc84e4eed219ceb99e155eb5accc040d7fabb3bd9de87a5135cb8852e283089e7ccff7fc90e0c541a30c5b2ac04c6b0c34f12e05bb295ec0e22297cfea2d2a3677d798d3d74be86f270c7d1d120473f27c5ec73eb6d31a1046c7033857598620cd5819b57df2a80404b10d843f3f8566d27b5e25e19ad9d8f3cbe29fd3bc81ebaa5e4cef1a482b108caf298f1fc04effb4f1487bafeb53381ab2242becd98679127a5a601fb3848f2133dd702a6fea0a67d44ebd58e87d929d93876df320475e4ae7dd78a82a3ea1380bccc0e6dc1948e61c15c1b2ddf35ff1308079927e15a7936d3892aa72eb59504fd9efbeeb20a2629ec9349c6a63baaa1439d5c1a244494ca6865d34d1ba75d8b9c5dd7aaeeeac982dd61f1bee0a74e8103a17d55f92f3f786340ff5d2fd6ec50b190a3805130154fd4a608fd9ea3bd30983321f8377f894e045c91107ab27dc45f982f97ae6edd6d4505cb01d45a0ac5401d1704d6640d0547ca4676fdb243d1d9a64b176dc8e67f0c88302c5a109b1d4e35d95848144deddb5eedc4dde0e5e094c4fc58d6d10df66943abba8f958f22786ed26f0f249e3a338ea904a360e3419ca677af1537e3294e1982e2a924aab9980d32db6e23127fbeb768898cb75e2beb661852766179413b590a0627c8a0be1adca00e65e7e2cff4e0d1d743505152fa5979d1e42736039822073ba6ab48f0943c9d0164ec1f18b072d1eb4e2c2d88e98657845d4b61c205cac3b4047fdb2aeb7e9091171e78f02171f57171f2c195adf9a021e6e515963cc356e258adbdd2f4d5f4ef167382de6179ebda563957f7b47576d9df6861a526a926defc1f5bdbcf9c559dcad184f9808b825e9c9bf633397dce61b4bf46cf48047842f10a51e44d162acdde7098ab7042ad3563a7f636f75dcfdc8c1720a85aa551608a624ca2f8532561c7c67c69cbed2deffd3da496b9c97e6c860f84e36656b85c56b88803a158c082383dbc63124866947e6a0cb275ea59cbd4b9bfe929f13341a4347ffe25893e42cdb57db6953ee7ce24aabb60ccc5a21d854538d7993debb5a6b486a7731b02e1b4fda794d243d4504fd1f6be04dd3c2a4f38bc28812bd01a070b84dcf892786eaea092e51a0a2acca4e466d347f2c4686eb9549db42bf1bcac7a3a7f1e70ea4539bb63f97198911a9cdc3bc7cbcff4a32d8da2e6b79b0daca10676bf75ea8d89e0a42e30272c40d7cc16adcd8df46290906fdafe49cd6056c3aa39bc8b0e07d0d796d7fd910aa8e0f5d839eec5a57d10c87749bb46b4632b89f254cf11b5aca9232a917d2f8f2a4c1ef401c4c264836119932d37427ad5cde746c5d55b20e2b5588c040f2a9d4201b13348ac84debe2399b079f6f02310b0ec2e2c162c578181205a0c82f2ae6655127c5cf032205f7de26ed0397d77d011d4f4441665e6e640157dac411cd3f98f180542a94ad2f0ae832de39cf16b457d738a986c178837353fd59959e5b97e664a5ba9fbcd34b7ba28658ee8b19b23058e6a8806ff5329a46a6b3c5a759d42d10c826d5fd5e153e6a96652a93d7cca937b324622822e1fe9274838e49290b22f9a2423186e12e0ba5590cb136e90d414a79131c30bbbbf5d8999da68690fd85e2b4a14e54f6bd0ec3b6d3adef09a63a720290c52b479b2d39743aeca87ff4195116c4485ed740af2741e6d27f2a61ee6037092d5347cf6cd752b25fb432fbb2c23b7f081802dfa4d108ee5619ba4214c16dcf89c6a0fbbf7c7a0873deba1ebaa839311fe552351e32c68e7cf40879303caec2c6ad1b91f975e742bb1ad3c73e69f54315c0bd137f010779b22610070f2c47f88a12f6aef017899f75d3505ffcca759c8be101d36307c7cffbc4e031b58a7818e4a9f276881631904917f2f3c161d6423d4751601c6a6b997f438f43c6385607b35411619b07b127e0a2b137b9d7ef344f124a0a0bfa42edba325017831a07dec03564102c6ddb7dcb63c7aa548b25dafec7be01569d32a1c511f8c50a451cf12501345ef4d83bfc0190ba1e06ab0aeb3150df2c894f95d9450a52a3b8dc0eaeb1d8a4e027615a74704338ace4fdfe21a45ade54baa665649b64b11fe467a1b6fe15ef44f04c4a0d4764656f17bb12e37271c5ce6d0f86c8daa609fb628a25298f48c9c2d9826e0618b981a8799afabcf93b451442a1d27998510fba6b8e185b8c1fe3dc031119a57d46e5ff8d4f00c541eb75ce1b62dff5eea5e4db452e648d8f2fb8df306880dd0f6244fb13b6ff008e85a3ea76166073a37756edd98a10e72750bf29cdafb94f5c65461a9cf52856857c9e30635210ead9fcf192d3d07ceab2e3f0346117230f462af6dbbaf735bc6d199cb30cff7c03fdb02959cabad11352200fd24e8328dde5f0bedf8ee2b5bbc876ebecdab49b106bd8a7626dd2824b5defbd8f4eea9f3eee493c464466f9fa4f741f3c361d7e342edcfb4a062bd05bf7371aff16441920e62d71f7fe70b183908df7c0c1912b7a7a55dce432db02e03c33d5516930a783330a0c241c94361a4fa882f895c76a63fdcf52b67ddb44184b6a5ec7466a0be0355ec4e6312e8878ed28248c18245b4b1506ab39bb6ef8e95117d139a02712eb206d468665f35fd4da516d0532acd62dd2666b08d7794902bdfd0a63200b708ebd55be1775061a127ede326c36b419477ffdeee3a42b7cf546b083651cf66d25024d8858ba09c555dfb1b20cb2b8267b6e8079b7cb611959cbf7b8329a87b737ef8238cf8e2726dd7462ff35217236e96ce7db645462b1e4398678591158a15a35f1d4c3885a299b0a008ca947f1a65de781652303befd7a9f7187e599707446a841afad1085a02fbd1d339bf8bd28aa6b98426b95ee796c5fbee06104bc19faabbdb1416c5cc981da37fb02ce9f86584b65c858f096530eaab8a53f7879543a6854f8b52647dc1652133c3e19f61aff2d47abc2da545accc935ad157dbb5f9300e669d30db89fbe2c875839ee857a99562463a9ae84f55556c3963aa7c2d64462e96ddcc4c74526c0cb0aa0db2360d1ca87dbbd1c5b31a28a9acc9dd2a7f9e088715c9f2b27bee620227cd7f02570c5a39404348760f41acb9fe684801b887a886fdcafa0a40a6e2a2c81a7c074015079b1ae8e474a31fb91403ba988d5caed4629b8f5c8dc47f6b3bfa203b62f0e1c8b08a425305bea30522bf4ed5526c6a0afd7d645ada3490e59d6eef19ba5d1d0320af0d4b2522577f85fec69527e174c54986768a83a87e71ef31d210db41f3cfcb296942ae0662';
console.log(sb(data));