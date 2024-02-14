document.addEventListener("DOMContentLoaded", function() {
    var textareaCounts = {};
    var selectedMethod = document.getElementById("method").value;

//    document.getElementById("selectedMethod").innerText = "Ви обрали метод: " + selectedMethod;

    updateInputFields(selectedMethod);

    document.getElementById("method").addEventListener("change", function() {
        selectedMethod = document.getElementById("method").value;
//        document.getElementById("selectedMethod").innerText = "Ви обрали метод: " + selectedMethod;

        updateInputFields(selectedMethod);
    });


    function updateInputFields(method) {
        document.getElementById("input_for_encrypt").innerHTML = "";
        if (['SHA-1', 'SHA-224', 'SHA-256', 'SHA-384', 'SHA-512', 'MD5'].includes(method) ||
            ['Historical method', 'Caesar (Latin)', 'Caesar (Cyrillic ukr)', 'Caesar (Cyrillic rus)',
            'Morse Code (Latin)', 'Homomorphism (Cyrillic rus)', 'Conversion', 'Binary', 'Hexadecimal (Latin)', 'Octal',
            'Decimal', 'Інщі', 'Fernet', 'Base64'].includes(method)) {
            addTextarea(method, textareaCounts[method] || 1);
        } else if (method === "Enigma (Latin)") {
            addEnigmaInputs();
        } else if (method === "Безус") {
            addBaseuse();
        }

    }

    function addTextarea(method, count) {
        var inputForEncrypt = document.getElementById("input_for_encrypt");

        for (var i = 0; i < count; i++) {
            var encrypt_code = document.createElement("textarea");
            encrypt_code.setAttribute("type", "text");
            encrypt_code.setAttribute("name", "input_for_encrypt");
            encrypt_code.setAttribute("placeholder", "Текст для метода " + method);
            encrypt_code.addEventListener("input", function() {
                console.log(this.value);
            });

            encrypt_code.style.backgroundColor = "#ffffcc";
            inputForEncrypt.appendChild(encrypt_code);
        }
    }

    function addEnigmaInputs() {
        for (var j = 1; j <= 3; j++) {
            var rotorInput = document.createElement("input");
            rotorInput.setAttribute("type", "number");
            rotorInput.setAttribute("name", "rotor" + (j));
            rotorInput.setAttribute("placeholder", "Ротор");
            document.getElementById("input_for_encrypt").appendChild(rotorInput);
        }
    }

});
