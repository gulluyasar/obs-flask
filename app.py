from flask import redirect, url_for

from views import app


@app.route("/")
def home():
    return redirect(url_for("giris-ekrani.login"))


# ilk güncelleme
#ikinci güncelleme

if __name__ == '__main__':
    app.run(debug=True)
