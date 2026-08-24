async function predictSales() {

    const temperature = document.getElementById("temperature").value;
    const result = document.getElementById("result");

    if (temperature === "") {
        result.innerHTML = "Please enter a temperature.";
        return;
    }

    try {

        const response = await fetch("http://127.0.0.1:5000/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                Temperature_C: Number(temperature)
            })
        });

        const data = await response.json();

        result.innerHTML =
            "Predicted Ice Cream Sales: " +
            data.Predicted_IceCream_Sales.toFixed(2);

    } catch (error) {

        result.innerHTML =
            "Error: API is not connected.";

        console.error(error);
    }
}