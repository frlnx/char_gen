let timer;
let turn = 0;

function sleep(ms, f) {
    return (
        setTimeout(f, ms)
    )
}


function loading() {
    timer = setInterval(turnLoader, 1 / 60);
    let x = document.getElementById("loader");
    x.classList.add("loaderVisible");
}

function loadingDone() {

    let x = document.getElementById("loader");
    x.classList.remove("loaderVisible");
    sleep(1000, () => {
        clearInterval(timer);
    });

}

function turnLoader() {
    let x = document.getElementById("loader");
    turn += 1;
    x.style.transform = "rotate(" + (turn % 360) + "deg)"
}

document.addEventListener("DOMContentLoaded", () => {
        const form = document.getElementById("characterForm");

        form.addEventListener("submit", async (event) => {
                // Prevent the default form submission
                event.preventDefault();

                loading();
                // Create a FormData object from the form
                const formData = new FormData(form);

                // Convert FormData to a plain JavaScript object
                const formObject = {};
                formData.forEach((value, key) => {
                    formObject[key] = value;
                });

                // Convert the object to a JSON string
                const formJSON = JSON.stringify(formObject);

                try {
                    // Send the JSON data to the server via fetch
                    const response = await fetch(form.action, {
                        method: form.method, // Typically "POST"
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: formJSON
                    });

                    // Wait for and process the response
                    const result = await response.text();
                    loadingDone()
                    sleep(1000, () => {
                        // Log the result to the console
                        var converter = new showdown.Converter(),
                            text = result,
                            html = converter.makeHtml(text);
                        document.getElementById("story").innerHTML = html;
                    });

                } catch (error) {
                    console.error("Error:", error);
                }
            }
        );

    }
);
