from flask import redirect, url_for

from views import app


@app.route("/")
def home():
    return redirect(url_for("giris-ekrani.login"))


# ogrendi giris 254097606
# scrypt:32768:8:1$MR4zZTQRtRMSeWen$fe227c89c10cb9618b7cbd20a4996d7c57c1232ef0326a09c901902a4ebea4efcc96e042e28bae58b718f283b709652e2c5da85e3726889023a71cebd641714a

if __name__ == '__main__':
    app.run(debug=True)
