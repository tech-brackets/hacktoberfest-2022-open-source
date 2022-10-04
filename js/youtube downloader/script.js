const form = document.getElementById("form");
const radio = document.getElementById("radioLink")
radio.addEventListener("click", e => {
    const link = e.target.value
    form.setAttribute("action", link)

})

form.addEventListener("submit", async e => {
    e.preventDefault();
    const loading = document.getElementById("loading");
    const judulVidio = document.getElementById("judulVidio")
    const elemenDownload = form.parentElement.querySelectorAll("a.dowload");
    const data = new FormData();
    loading.style.display = "block"
    data.append('link', document.querySelector("#form input").value);

    if (elemenDownload.length > 0) Array.from(elemenDownload).map(e => e.remove())

    try {
        const fect = await fetch(form.action, {
            method: "POST",
            body: data
        });
        const respon = await fect.json();
        const linkDownload = respon.result;
        let i = 1
        judulVidio.innerText = respon.title
        for (const key in linkDownload) {
            const download = document.createElement("a")
            const formParent = form.parentElement;
            download.setAttribute("href", linkDownload[key])
            download.setAttribute("class", "dowload")
            download.innerText = `Dowload link ${i} :${key}`
            formParent.appendChild(download)
            i++
        }
    } catch (error) {
        console.log(error);

    } finally {
        loading.style.display = "none"

    }
});