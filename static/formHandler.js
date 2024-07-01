document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("characterForm");

    form.addEventListener("submit", async (event) => {
        // Prevent the default form submission
        event.preventDefault();

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
            const result = await response.json();

            // Log the result to the console
            console.log(result);

        } catch (error) {
            console.error("Error:", error);
        }
    }
    );
}
);