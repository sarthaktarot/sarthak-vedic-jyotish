from flask import Flask, render_template_string, request, redirect, url_for, session

app = Flask(__name__)

# 🔐 WEBSITE PASSWORD
app.secret_key = "sarthak-vedic-secret-key-2026"
PASSWORD = "sarthak.vedic2026"


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        entered_password = request.form.get("password", "")

        if entered_password == PASSWORD:
            session["logged_in"] = True
            return redirect(url_for("home"))

        return """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Wrong Password</title>
            <style>
                body {
                    background:#08051c;
                    color:white;
                    font-family:Arial,sans-serif;
                    text-align:center;
                    padding-top:120px;
                }
                .box {
                    max-width:500px;
                    margin:auto;
                    padding:35px;
                    border-radius:20px;
                    background:rgba(255,255,255,.08);
                    box-shadow:0 0 30px rgba(255,216,107,.15);
                }
                a {
                    color:#ffd86b;
                    text-decoration:none;
                    font-weight:bold;
                }
            </style>
        </head>
        <body>
            <div class="box">
                <h1>❌ Wrong Password</h1>
                <p>Please enter the correct password.</p>
                <p><a href="/login">Try Again</a></p>
            </div>
        </body>
        </html>
        """

    return """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>🔐 Password Required</title>
        <style>
            * { box-sizing:border-box; }
            body {
                margin:0;
                min-height:100vh;
                display:flex;
                align-items:center;
                justify-content:center;
                background:
                    radial-gradient(circle at 20% 20%,#432080 0,transparent 32%),
                    radial-gradient(circle at 80% 30%,#0d5c78 0,transparent 30%),
                    radial-gradient(circle at 50% 90%,#72134f 0,transparent 32%),
                    #08051c;
                color:white;
                font-family:Arial,"Noto Sans Devanagari",sans-serif;
                overflow:hidden;
            }
            .login-box {
                width:min(92%,500px);
                padding:42px 32px;
                text-align:center;
                border:1px solid rgba(255,216,107,.35);
                border-radius:25px;
                background:rgba(8,5,28,.78);
                backdrop-filter:blur(12px);
                box-shadow:0 0 30px rgba(255,216,107,.12),
                           0 0 80px rgba(120,60,220,.16);
            }
            h1 {
                color:#ffd86b;
                font-size:clamp(28px,6vw,42px);
                margin-bottom:10px;
            }
            p {
                color:#ddd;
                font-size:17px;
            }
            input {
                width:100%;
                padding:15px;
                margin:18px 0 12px;
                border:1px solid rgba(255,216,107,.4);
                border-radius:12px;
                background:rgba(255,255,255,.08);
                color:white;
                font-size:17px;
                outline:none;
            }
            input:focus {
                border-color:#ffd86b;
                box-shadow:0 0 12px rgba(255,216,107,.2);
            }
            button {
                width:100%;
                padding:15px;
                border:none;
                border-radius:12px;
                background:linear-gradient(135deg,#ffd86b,#f0a93b);
                color:#1b1025;
                font-size:18px;
                font-weight:bold;
                cursor:pointer;
            }
            button:hover {
                transform:translateY(-1px);
                box-shadow:0 0 18px rgba(255,216,107,.35);
            }
        </style>
    </head>
    <body>
        <div class="login-box">
            <h1>🔐 सार्थक वैदिक ज्योतिष</h1>
            <p>This website is password protected.</p>

            <form method="POST">
                <input type="password"
                       name="password"
                       placeholder="Enter password"
                       autocomplete="current-password"
                       required>
                <button type="submit">🔓 Enter Website</button>
            </form>
        </div>
    </body>
    </html>
    """


@app.before_request
def protect_website():
    allowed_endpoints = {"login", "static"}

    if request.endpoint not in allowed_endpoints and not session.get("logged_in"):
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


HTML = r"""
<!DOCTYPE html>
<html lang="hi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>सार्थक वैदिक ज्योतिष</title>

<style>
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

html {
    scroll-behavior: smooth;
}

body {
    font-family: Arial, "Noto Sans Devanagari", sans-serif;
    background: #08051c;
    color: white;
    overflow-x: hidden;
}

/* BACKGROUND */
body::before {
    content: "";
    position: fixed;
    inset: 0;
    background:
        radial-gradient(circle at 20% 20%, #432080 0, transparent 30%),
        radial-gradient(circle at 80% 30%, #0d5c78 0, transparent 28%),
        radial-gradient(circle at 50% 90%, #72134f 0, transparent 30%);
    z-index: -2;
}

.stars {
    position: fixed;
    inset: 0;
    z-index: -1;
    background-image:
        radial-gradient(white 1px, transparent 1px),
        radial-gradient(#aaa 1px, transparent 1px);
    background-size: 80px 80px, 130px 130px;
    animation: moveStars 30s linear infinite;
    opacity: .45;
}

@keyframes moveStars {
    from { transform: translateY(0); }
    to { transform: translateY(80px); }
}

/* HEADER */
header {
    position: sticky;
    top: 0;
    z-index: 100;
    padding: 15px 5%;
    background: rgba(7, 4, 25, .9);
    backdrop-filter: blur(12px);
    border-bottom: 1px solid rgba(255,255,255,.15);
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.logo {
    font-size: 25px;
    font-weight: 900;
    color: #ffd86b;
}

nav {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    justify-content: center;
}

nav button {
    border: none;
    padding: 10px 14px;
    border-radius: 20px;
    background: rgba(255,255,255,.1);
    color: white;
    cursor: pointer;
    font-weight: bold;
    transition: .3s;
}

nav button:hover {
    background: #ffd86b;
    color: #160b2c;
    transform: translateY(-2px);
}

/* HERO */
.hero {
    min-height: 88vh;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 50px 20px;
}

.hero-box {
    max-width: 1000px;
    animation: fadeUp 1.2s ease;
}

.om {
    font-size: 70px;
    color: #ffd86b;
    animation: float 3s ease-in-out infinite;
}

.hero h1 {
    font-size: clamp(42px, 8vw, 85px);
    color: #ffd86b;
    text-shadow: 0 0 30px rgba(255,216,107,.5);
    margin: 15px 0;
}

.hero h2 {
    font-size: 28px;
    margin-bottom: 15px;
}

.hero p {
    font-size: 19px;
    color: #ddd;
    line-height: 1.8;
}

.main-btn {
    margin-top: 30px;
    padding: 15px 30px;
    border: none;
    border-radius: 30px;
    background: linear-gradient(90deg,#ffd86b,#ff9e45);
    color: #1a0d27;
    font-size: 18px;
    font-weight: bold;
    cursor: pointer;
    transition: .3s;
}

.main-btn:hover {
    transform: scale(1.08);
    box-shadow: 0 0 25px rgba(255,216,107,.6);
}

/* SECTIONS */
section {
    padding: 80px 6%;
}

.section-title {
    text-align: center;
    font-size: 42px;
    color: #ffd86b;
    margin-bottom: 40px;
}

.intro {
    max-width: 900px;
    margin: auto;
    text-align: center;
    font-size: 18px;
    line-height: 2;
    color: #ddd;
}

/* CARDS */
.grid {
    max-width: 1200px;
    margin: auto;
    display: grid;
    grid-template-columns: repeat(auto-fit,minmax(220px,1fr));
    gap: 22px;
}

.card {
    background: rgba(255,255,255,.08);
    border: 1px solid rgba(255,255,255,.13);
    border-radius: 22px;
    padding: 25px;
    transition: .35s;
    backdrop-filter: blur(8px);
}

.card:hover {
    transform: translateY(-8px) scale(1.02);
    box-shadow: 0 15px 35px rgba(0,0,0,.4);
    border-color: #ffd86b;
}

.card h3 {
    color: #ffd86b;
    font-size: 24px;
    margin-bottom: 12px;
}

.card p {
    color: #ddd;
    line-height: 1.7;
}

.number {
    font-size: 38px;
    color: #ffae5c;
    font-weight: bold;
}

/* PLANETS */
.planet {
    text-align: center;
}

.planet-icon {
    font-size: 48px;
    margin-bottom: 10px;
    animation: float 3s ease-in-out infinite;
}

/* KUNDLI */
.kundli-container {
    display: flex;
    justify-content: center;
    margin-top: 30px;
}

.kundli {
    width: 440px;
    height: 440px;
    max-width: 90vw;
    max-height: 90vw;
    position: relative;
    border: 3px solid #ffd86b;
    transform: rotate(45deg);
    background: rgba(255,255,255,.04);
    box-shadow: 0 0 35px rgba(255,216,107,.25);
}

.kundli::before,
.kundli::after {
    content: "";
    position: absolute;
    inset: 0;
    border: 2px solid #ffd86b;
}

.kundli::before {
    transform: rotate(45deg) scale(.71);
}

.kundli::after {
    transform: rotate(90deg) scale(.71);
}

.kundli-center {
    position: absolute;
    width: 100px;
    height: 100px;
    left: 50%;
    top: 50%;
    transform: translate(-50%,-50%) rotate(-45deg);
    border: 2px solid #ffd86b;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #ffd86b;
    font-weight: bold;
}

/* LEARNING */
.learn-box {
    max-width: 1000px;
    margin: auto;
}

.learn-step {
    margin-bottom: 15px;
    padding: 20px;
    border-radius: 15px;
    background: rgba(255,255,255,.07);
    border-left: 5px solid #ffd86b;
}

.learn-step h3 {
    color: #ffd86b;
    margin-bottom: 8px;
}

/* QUIZ */
.quiz-box {
    max-width: 800px;
    margin: auto;
    padding: 35px;
    background: rgba(255,255,255,.08);
    border-radius: 25px;
    text-align: center;
}

.question {
    font-size: 25px;
    margin-bottom: 25px;
}

.options {
    display: grid;
    gap: 12px;
}

.options button {
    padding: 15px;
    border: none;
    border-radius: 12px;
    cursor: pointer;
    background: rgba(255,255,255,.12);
    color: white;
    font-size: 17px;
    transition: .25s;
}

.options button:hover {
    background: #ffd86b;
    color: #160b2c;
}

#feedback {
    margin-top: 20px;
    font-size: 20px;
    font-weight: bold;
}

/* FOOTER */
footer {
    text-align: center;
    padding: 35px;
    background: rgba(0,0,0,.35);
    color: #ccc;
}

footer strong {
    color: #ffd86b;
}

/* ANIMATIONS */
@keyframes float {
    0%,100% { transform: translateY(0); }
    50% { transform: translateY(-12px); }
}

@keyframes fadeUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* ENHANCED COSMIC + ZODIAC WALLPAPER */
body { background: radial-gradient(circle at 50% 45%, rgba(76,28,120,.22), transparent 38%), #08051c; }
body::before { animation: cosmicBackground 14s ease-in-out infinite alternate; }
.stars { background-image: radial-gradient(circle,rgba(255,255,255,.95) 1px,transparent 1.5px),radial-gradient(circle,rgba(255,216,107,.75) 1px,transparent 1.5px),radial-gradient(circle,rgba(170,120,255,.65) 1px,transparent 1.5px); background-size:75px 75px,125px 125px,180px 180px; animation:moveStars 30s linear infinite,starPulse 5s ease-in-out infinite alternate; }
.zodiac-wallpaper{position:fixed;inset:0;z-index:-1;overflow:hidden;pointer-events:none}.zodiac-wallpaper span{position:absolute;color:rgba(255,216,107,.28);font-size:clamp(28px,4vw,52px);font-weight:bold;text-shadow:0 0 8px rgba(255,216,107,.45),0 0 22px rgba(150,80,255,.35);animation:zodiacFloat 9s ease-in-out infinite}.zodiac-wallpaper span:nth-child(1){left:5%;top:14%}.zodiac-wallpaper span:nth-child(2){left:18%;top:48%;animation-delay:1.2s}.zodiac-wallpaper span:nth-child(3){left:34%;top:18%;animation-delay:2.4s}.zodiac-wallpaper span:nth-child(4){left:52%;top:72%;animation-delay:3.6s}.zodiac-wallpaper span:nth-child(5){left:70%;top:20%;animation-delay:4.8s}.zodiac-wallpaper span:nth-child(6){left:88%;top:46%;animation-delay:6s}.zodiac-wallpaper span:nth-child(7){left:8%;top:82%;animation-delay:7.2s}.zodiac-wallpaper span:nth-child(8){left:27%;top:88%;animation-delay:8.4s}.zodiac-wallpaper span:nth-child(9){left:43%;top:43%;animation-delay:1.8s}.zodiac-wallpaper span:nth-child(10){left:62%;top:10%;animation-delay:3s}.zodiac-wallpaper span:nth-child(11){left:78%;top:82%;animation-delay:5.4s}.zodiac-wallpaper span:nth-child(12){left:94%;top:70%;animation-delay:6.6s}
.cosmic-orb{position:fixed;width:260px;height:260px;border-radius:50%;pointer-events:none;z-index:-2;filter:blur(3px);opacity:.22;background:radial-gradient(circle,#ffd86b 0,rgba(255,130,40,.25) 30%,transparent 70%)}.orb-one{left:-100px;top:35%;animation:orbOne 18s ease-in-out infinite alternate}.orb-two{right:-100px;top:55%;background:radial-gradient(circle,#8c5cff 0,rgba(60,80,255,.2) 30%,transparent 70%);animation:orbTwo 22s ease-in-out infinite alternate}
@keyframes cosmicBackground{0%{transform:scale(1);opacity:.78}100%{transform:scale(1.12);opacity:1}}@keyframes starPulse{0%{opacity:.32}100%{opacity:.62}}@keyframes zodiacFloat{0%,100%{transform:translate3d(0,0,0) rotate(-4deg) scale(1);opacity:.18}50%{transform:translate3d(18px,-28px,0) rotate(8deg) scale(1.15);opacity:.62}}@keyframes orbOne{0%{transform:translate(0,0) scale(.8)}100%{transform:translate(38vw,-12vh) scale(1.3)}}@keyframes orbTwo{0%{transform:translate(0,0) scale(1)}100%{transform:translate(-35vw,12vh) scale(1.35)}}
/* MOBILE */
@media(max-width:750px) {
    header {
        flex-direction: column;
        gap: 12px;
    }

    .logo {
        font-size: 21px;
    }

    .section-title {
        font-size: 32px;
    }

    .hero h1 {
        font-size: 45px;
    }

    .kundli {
        width: 320px;
        height: 320px;
    }
}
</style>
</head>

<body>

<div class="stars"></div>

<div class="zodiac-wallpaper" aria-hidden="true">
    <span>♈</span><span>♉</span><span>♊</span><span>♋</span><span>♌</span><span>♍</span>
    <span>♎</span><span>♏</span><span>♐</span><span>♑</span><span>♒</span><span>♓</span>
</div>
<div class="cosmic-orb orb-one" aria-hidden="true"></div>
<div class="cosmic-orb orb-two" aria-hidden="true"></div>

<header>

    <div class="logo">
        🔱 सार्थक वैदिक ज्योतिष
    </div>

    <nav>
        <button onclick="go('home')">मुख्य पृष्ठ</button>
        <button onclick="go('rashi')">राशियाँ</button>
        <button onclick="go('planets')">ग्रह</button>
        <button onclick="go('bhav')">भाव</button>
        <button onclick="go('kundli')">कुंडली</button>
        <button onclick="go('learn')">सीखें</button>
        <button onclick="go('quiz')">क्विज़</button>
    </nav>

</header>


<!-- HOME -->

<section class="hero" id="home">

    <div class="hero-box">

        <div class="om">ॐ</div>

        <h1>सार्थक वैदिक ज्योतिष</h1>

        <h2>SARTHAK VEDIC JYOTISH</h2>

        <p>
            वैदिक ज्योतिष को सरल तरीके से सीखने और समझने की एक
            शैक्षिक वेबसाइट।
        </p>

        <p>
            राशि • ग्रह • भाव • कुंडली • नक्षत्र • दशा • गोचर
        </p>

        <button class="main-btn" onclick="go('learn')">
            ✨ ज्योतिष सीखना शुरू करें
        </button>

    </div>

</section>


<!-- INTRO -->

<section>

    <h2 class="section-title">🔮 वैदिक ज्योतिष क्या है?</h2>

    <p class="intro">
        वैदिक ज्योतिष जन्म के समय आकाश में ग्रहों और राशियों की
        स्थिति को समझने की एक ज्योतिषीय प्रणाली है।
        जन्म कुंडली में ग्रह, राशि और भाव की स्थिति को देखकर
        अलग-अलग जीवन क्षेत्रों का अध्ययन किया जाता है।
    </p>

</section>


<!-- RASHI -->

<section id="rashi">

    <h2 class="section-title">♈ 12 राशियाँ</h2>

    <div class="grid">

        <div class="card"><div class="number">01</div><h3>♈ मेष</h3><p>राशिचक्र की पहली राशि।</p></div>

        <div class="card"><div class="number">02</div><h3>♉ वृषभ</h3><p>राशिचक्र की दूसरी राशि।</p></div>

        <div class="card"><div class="number">03</div><h3>♊ मिथुन</h3><p>राशिचक्र की तीसरी राशि।</p></div>

        <div class="card"><div class="number">04</div><h3>♋ कर्क</h3><p>राशिचक्र की चौथी राशि।</p></div>

        <div class="card"><div class="number">05</div><h3>♌ सिंह</h3><p>राशिचक्र की पाँचवीं राशि।</p></div>

        <div class="card"><div class="number">06</div><h3>♍ कन्या</h3><p>राशिचक्र की छठी राशि।</p></div>

        <div class="card"><div class="number">07</div><h3>♎ तुला</h3><p>राशिचक्र की सातवीं राशि।</p></div>

        <div class="card"><div class="number">08</div><h3>♏ वृश्चिक</h3><p>राशिचक्र की आठवीं राशि।</p></div>

        <div class="card"><div class="number">09</div><h3>♐ धनु</h3><p>राशिचक्र की नौवीं राशि।</p></div>

        <div class="card"><div class="number">10</div><h3>♑ मकर</h3><p>राशिचक्र की दसवीं राशि।</p></div>

        <div class="card"><div class="number">11</div><h3>♒ कुंभ</h3><p>राशिचक्र की ग्यारहवीं राशि।</p></div>

        <div class="card"><div class="number">12</div><h3>♓ मीन</h3><p>राशिचक्र की बारहवीं राशि।</p></div>

    </div>

</section>


<!-- PLANETS -->

<section id="planets">

    <h2 class="section-title">🪐 नवग्रह</h2>

    <div class="grid">

        <div class="card planet">
            <div class="planet-icon">☀️</div>
            <h3>सूर्य</h3>
            <p>आत्मविश्वास, व्यक्तित्व और नेतृत्व से जुड़ा ग्रह।</p>
        </div>

        <div class="card planet">
            <div class="planet-icon">🌙</div>
            <h3>चंद्र</h3>
            <p>मन, भावनाओं और मानसिक स्थिति से जुड़ा ग्रह।</p>
        </div>

        <div class="card planet">
            <div class="planet-icon">☊</div>
            <h3>मंगल</h3>
            <p>ऊर्जा, साहस और कार्य करने की शक्ति से जुड़ा ग्रह।</p>
        </div>

        <div class="card planet">
            <div class="planet-icon">☿</div>
            <h3>बुध</h3>
            <p>बुद्धि, संचार और सीखने से जुड़ा ग्रह।</p>
        </div>

        <div class="card planet">
            <div class="planet-icon">🟡</div>
            <h3>गुरु</h3>
            <p>ज्ञान, शिक्षा और विस्तार से जुड़ा ग्रह।</p>
        </div>

        <div class="card planet">
            <div class="planet-icon">♀</div>
            <h3>शुक्र</h3>
            <p>सुख, कला, आकर्षण और संबंधों से जुड़ा ग्रह।</p>
        </div>

        <div class="card planet">
            <div class="planet-icon">♄</div>
            <h3>शनि</h3>
            <p>अनुशासन, कर्म, धैर्य और जिम्मेदारी से जुड़ा ग्रह।</p>
        </div>

        <div class="card planet">
            <div class="planet-icon">☊</div>
            <h3>राहु</h3>
            <p>इच्छा, महत्वाकांक्षा और भौतिक आकर्षण से जुड़ा छाया ग्रह।</p>
        </div>

        <div class="card planet">
            <div class="planet-icon">☋</div>
            <h3>केतु</h3>
            <p>वैराग्य, आध्यात्मिकता और अलगाव से जुड़ा छाया ग्रह।</p>
        </div>

    </div>

</section>


<!-- BHAV -->

<section id="bhav">

    <h2 class="section-title">🏠 12 भाव</h2>

    <div class="grid">

        <div class="card"><h3>1️⃣ प्रथम भाव</h3><p>स्वयं, व्यक्तित्व और शरीर।</p></div>

        <div class="card"><h3>2️⃣ द्वितीय भाव</h3><p>धन, परिवार और वाणी।</p></div>

        <div class="card"><h3>3️⃣ तृतीय भाव</h3><p>साहस, प्रयास और छोटे भाई-बहन।</p></div>

        <div class="card"><h3>4️⃣ चतुर्थ भाव</h3><p>घर, माता और सुख।</p></div>

        <div class="card"><h3>5️⃣ पंचम भाव</h3><p>बुद्धि, शिक्षा और संतान।</p></div>

        <div class="card"><h3>6️⃣ षष्ठ भाव</h3><p>रोग, ऋण और शत्रु।</p></div>

        <div class="card"><h3>7️⃣ सप्तम भाव</h3><p>विवाह और साझेदारी।</p></div>

        <div class="card"><h3>8️⃣ अष्टम भाव</h3><p>परिवर्तन, रहस्य और आयु।</p></div>

        <div class="card"><h3>9️⃣ नवम भाव</h3><p>भाग्य, धर्म और उच्च शिक्षा।</p></div>

        <div class="card"><h3>🔟 दशम भाव</h3><p>कर्म, करियर और प्रतिष्ठा।</p></div>

        <div class="card"><h3>1️⃣1️⃣ एकादश भाव</h3><p>लाभ, आय और इच्छाओं की पूर्ति।</p></div>

        <div class="card"><h3>1️⃣2️⃣ द्वादश भाव</h3><p>व्यय, विदेश और मोक्ष।</p></div>

    </div>

</section>


<!-- KUNDLI -->

<section id="kundli">

    <h2 class="section-title">🔷 जन्म कुंडली</h2>

    <p class="intro">
        जन्म कुंडली जन्म के समय ग्रहों की स्थिति को दर्शाने वाला
        ज्योतिषीय चार्ट है।
    </p>

    <div class="kundli-container">

        <div class="kundli">

            <div class="kundli-center">
                लग्न
            </div>

        </div>

    </div>

</section>


<!-- LEARN -->

<section id="learn">

    <h2 class="section-title">📚 वैदिक ज्योतिष सीखने का क्रम</h2>

    <div class="learn-box">

        <div class="learn-step">
            <h3>01. वैदिक ज्योतिष</h3>
            <p>ज्योतिष की मूल अवधारणा को समझें।</p>
        </div>

        <div class="learn-step">
            <h3>02. जन्म कुंडली</h3>
            <p>कुंडली और उसके मुख्य भागों को समझें।</p>
        </div>

        <div class="learn-step">
            <h3>03. 12 राशियाँ</h3>
            <p>बारह राशियों और उनके स्वभाव को सीखें।</p>
        </div>

        <div class="learn-step">
            <h3>04. नवग्रह</h3>
            <p>नौ ग्रहों के अर्थ और प्रभाव को समझें।</p>
        </div>

        <div class="learn-step">
            <h3>05. 12 भाव</h3>
            <p>कुंडली के बारह भावों के जीवन क्षेत्रों को जानें।</p>
        </div>

        <div class="learn-step">
            <h3>06. लग्न</h3>
            <p>लग्न और उसके महत्व को समझें।</p>
        </div>

        <div class="learn-step">
            <h3>07. राशि स्वामी</h3>
            <p>हर राशि के स्वामी ग्रह को जानें।</p>
        </div>

        <div class="learn-step">
            <h3>08. ग्रहों की दृष्टि</h3>
            <p>ग्रहों की दृष्टि का अध्ययन करें।</p>
        </div>

        <div class="learn-step">
            <h3>09. नक्षत्र</h3>
            <p>नक्षत्र और उनके पाद को समझें।</p>
        </div>

        <div class="learn-step">
            <h3>10. उच्च और नीच</h3>
            <p>ग्रहों की उच्च और नीच स्थिति को समझें।</p>
        </div>

        <div class="learn-step">
            <h3>11. दशा</h3>
            <p>ग्रहों की दशाओं का अध्ययन करें।</p>
        </div>

        <div class="learn-step">
            <h3>12. गोचर</h3>
            <p>ग्रहों की वर्तमान गति और गोचर को समझें।</p>
        </div>

        <div class="learn-step">
            <h3>13. योग</h3>
            <p>कुंडली में बनने वाले योगों को समझें।</p>
        </div>

        <div class="learn-step">
            <h3>14. ग्रहों की शक्ति</h3>
            <p>ग्रहों की शक्ति का अध्ययन करें।</p>
        </div>

        <div class="learn-step">
            <h3>15. वर्ग कुंडलियाँ</h3>
            <p>विभिन्न वर्ग कुंडलियों को समझें।</p>
        </div>

        <div class="learn-step">
            <h3>16. नक्षत्र पाद</h3>
            <p>नक्षत्रों के पादों का अध्ययन करें।</p>
        </div>

        <div class="learn-step">
            <h3>17. मुहूर्त</h3>
            <p>उचित समय चुनने की अवधारणा समझें।</p>
        </div>

        <div class="learn-step">
            <h3>18. प्रश्न ज्योतिष</h3>
            <p>प्रश्न के आधार पर ज्योतिषीय अध्ययन समझें।</p>
        </div>

        <div class="learn-step">
            <h3>19. पंचांग</h3>
            <p>पंचांग के प्रमुख अंगों को जानें।</p>
        </div>

        <div class="learn-step">
            <h3>20. सूर्य • चंद्र • लग्न</h3>
            <p>इन तीनों की भूमिका को समझें।</p>
        </div>

    </div>

</section>


<!-- QUIZ -->

<section id="quiz">

    <h2 class="section-title">🧠 ज्योतिष क्विज़</h2>

    <div class="quiz-box">

        <div class="question" id="question">
            प्रश्न लोड हो रहा है...
        </div>

        <div class="options" id="options"></div>

        <div id="feedback"></div>

        <button class="main-btn" onclick="nextQuestion()">
            अगला प्रश्न
        </button>

        <p style="margin-top:20px;">
            स्कोर: <span id="score">0</span>
        </p>

    </div>

</section>


<footer>

    <strong>🔱 सार्थक वैदिक ज्योतिष</strong>

    <p style="margin-top:10px;">
        वैदिक ज्योतिष सीखने के लिए शैक्षिक वेबसाइट
    </p>

</footer>


<script>

function go(id) {
    document.getElementById(id).scrollIntoView({
        behavior: "smooth"
    });
}


/* QUIZ */

const quiz = [

    {
        q: "वैदिक ज्योतिष में जन्म के समय ग्रहों की स्थिति किसमें दिखाई जाती है?",
        options: ["जन्म कुंडली", "पंचांग", "नक्षत्र", "दशा"],
        answer: 0
    },

    {
        q: "राशिचक्र में कुल कितनी राशियाँ होती हैं?",
        options: ["9", "10", "12", "27"],
        answer: 2
    },

    {
        q: "वैदिक ज्योतिष में कुल कितने नवग्रह माने जाते हैं?",
        options: ["7", "8", "9", "12"],
        answer: 2
    },

    {
        q: "प्रथम भाव मुख्य रूप से किससे संबंधित है?",
        options: ["लाभ", "स्वयं और व्यक्तित्व", "विदेश", "विवाह"],
        answer: 1
    },

    {
        q: "दशम भाव मुख्य रूप से किससे संबंधित है?",
        options: ["कर्म और करियर", "भाई-बहन", "व्यय", "परिवार"],
        answer: 0
    },

    {
        q: "नवम भाव किससे जुड़ा माना जाता है?",
        options: ["भाग्य", "रोग", "वाणी", "व्यय"],
        answer: 0
    },

    {
        q: "कुंडली पढ़ने में किन चीजों को साथ देखा जाता है?",
        options: [
            "केवल ग्रह",
            "केवल राशि",
            "ग्रह, राशि और भाव आदि",
            "केवल लग्न"
        ],
        answer: 2
    },

    {
        q: "राशिचक्र की पहली राशि कौन-सी है?",
        options: ["मेष", "वृषभ", "मिथुन", "कर्क"],
        answer: 0
    }

];

let current = 0;
let score = 0;

function loadQuestion() {

    const q = quiz[current];

    document.getElementById("question").innerText =
        (current + 1) + ". " + q.q;

    const box = document.getElementById("options");

    box.innerHTML = "";

    document.getElementById("feedback").innerText = "";

    q.options.forEach((option, index) => {

        const btn = document.createElement("button");

        btn.innerText = option;

        btn.onclick = function() {

            if (index === q.answer) {

                document.getElementById("feedback").innerText =
                    "✅ सही उत्तर!";

                score++;

                document.getElementById("score").innerText = score;

            } else {

                document.getElementById("feedback").innerText =
                    "❌ गलत उत्तर! सही उत्तर: " + q.options[q.answer];

            }

        };

        box.appendChild(btn);

    });

}

function nextQuestion() {

    current++;

    if (current >= quiz.length) {

        document.getElementById("question").innerText =
            "🎉 क्विज़ पूरा हो गया!";

        document.getElementById("options").innerHTML = "";

        document.getElementById("feedback").innerText =
            "आपका अंतिम स्कोर: " + score + " / " + quiz.length;

        current = 0;

        return;
    }

    loadQuestion();
}

loadQuestion();

</script>

</body>
</html>
"""


@app.route("/")
@app.route("/sarthak")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    print("=" * 55)
    print("🔱 सार्थक वैदिक ज्योतिष वेबसाइट")
    print("=" * 55)
    print("वेबसाइट खोलें:")
    print("http://localhost:5000/sarthak")
    print("=" * 55)

    app.run(host="127.0.0.1", port=5000, debug=True)
