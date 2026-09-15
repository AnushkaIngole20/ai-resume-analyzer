const uploadBox = document.getElementById("uploadBox");
const resumeInput = document.getElementById("resume");
const fileName = document.getElementById("fileName");
const analyzeButton = document.getElementById("analyzeButton");


if (resumeInput) {

    resumeInput.addEventListener("change", function () {

        if (this.files.length > 0) {

            const file = this.files[0];

            if (file.type !== "application/pdf") {

                fileName.textContent =
                    "⚠️ Please select a PDF file.";

                fileName.style.color = "#fca5a5";

                this.value = "";

                return;
            }

            fileName.textContent =
                "✓ " + file.name;

            fileName.style.color = "#67e8f9";
        }

    });

}


/* Drag and drop */

if (uploadBox) {

    uploadBox.addEventListener(
        "dragover",
        function (event) {

            event.preventDefault();

            uploadBox.classList.add("dragover");

        }
    );


    uploadBox.addEventListener(
        "dragleave",
        function () {

            uploadBox.classList.remove("dragover");

        }
    );


    uploadBox.addEventListener(
        "drop",
        function (event) {

            event.preventDefault();

            uploadBox.classList.remove("dragover");

            const files = event.dataTransfer.files;

            if (files.length > 0) {

                const file = files[0];

                if (file.type === "application/pdf") {

                    resumeInput.files = files;

                    fileName.textContent =
                        "✓ " + file.name;

                    fileName.style.color =
                        "#67e8f9";

                } else {

                    fileName.textContent =
                        "⚠️ Only PDF files are allowed.";

                    fileName.style.color =
                        "#fca5a5";

                }

            }

        }
    );

}


/* Loading effect */

const form = document.querySelector("form");


if (form && analyzeButton) {

    form.addEventListener("submit", function () {

        analyzeButton.classList.add("loading");

        analyzeButton.innerHTML =
            "🧠 Analyzing Resume...";

        analyzeButton.disabled = true;

    });

}