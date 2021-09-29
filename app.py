from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def address_main():
    if request.method == "POST":
        resp = request.form
        dist1 = resp.get("city1")
        dist1 = dist1.lower()
        dist2 = resp.get("city2")
        dist2 = dist2.lower()
        tal1 = resp.get("Tq1")
        tal1 = tal1.lower()
        tal2 = resp.get("Tq2")
        tal2 = tal2.lower()
        a = 0

        if (dist1 == dist2):

            a = "they are from same district"

            if (tal1 == tal2):
                a= "they are from same district as well as same Taluka"

            else:
                a= "they are from same city but from diffrent taluka "

        return render_template("result.html", resp=a, city1=dist1, city2=dist2, Tq1=tal1, Tq2=tal2)

    else:
        return render_template("input.html")


if __name__ == '__main__':
    app.run(debug=True)