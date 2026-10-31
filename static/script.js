//wait for the page to load
document.addEventListener("ContentLoaded", () => {
    const inputField = document.getElementById("password-input")
    const resultBox = document.getElementById("result");

    // when input is being interacted with
    inputField.addEventListener("input", async () => {
        const password = inputField.value;

        if(password === "") {
            resultBox.textContent = "Start typing to check strength."
            resultBox.className = "result";
            return;
        }
        

        //send data to the backend 
        try {
            const response = await fetch("/api/check", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({password: password})
            });

            const data = await response.json();
            
            //show result
            resultBox.textContent = data.message + (data.feedback.length > 0 
                ? " (" + data.feedback.join(", ") + ")" 
                : "");
            
            //changes css class
            resultBox.className = "result " + data.status;

        } catch (error) {
            console.error("Error communicating with server:", error);
        }
    });
});



document.querySelectorAll("details").forEach((details) => {
    details.addEventListener("toggle", () => {
        if (!details.open) return;

        const content = details.querySelector(".tutorial-content");
        if (!content) return;

        content.style.animation = "none";
        void content.offsetWidth; // Force the browser to apply the reset
        content.style.animation = "";
    });
});
