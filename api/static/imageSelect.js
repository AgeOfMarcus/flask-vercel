window.onload = function() {
    var form = document.getElementById("image-form")
    var imageSelect = document.getElementById("imageSelect")
    imageSelect.value = ""
    imageSelect.addEventListener("change", function() {
        if (imageSelect.files.length > 0) {
            form.submit()
        }
    })
}