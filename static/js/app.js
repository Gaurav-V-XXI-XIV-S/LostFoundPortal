document.addEventListener("DOMContentLoaded", () => {
    if (window.AOS) {
        AOS.init({ duration: 650, once: true, offset: 80 });
    }

    document.querySelectorAll("input[type='file'][data-preview]").forEach((input) => {
        input.addEventListener("change", (event) => {
            const file = event.target.files && event.target.files[0];
            const preview = document.getElementById(input.dataset.preview);
            if (!file || !preview) return;

            const reader = new FileReader();
            reader.onload = (readerEvent) => {
                preview.src = readerEvent.target.result;
                const uploadBox = input.closest(".upload-box");
                if (uploadBox) uploadBox.classList.add("has-preview");
            };
            reader.readAsDataURL(file);
        });
    });

    setTimeout(() => {
        document.querySelectorAll(".alert").forEach((alert) => {
            const instance = bootstrap.Alert.getOrCreateInstance(alert);
            instance.close();
        });
    }, 4500);
});
