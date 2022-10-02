function sort(val) {
    const index = (isNaN(val) ? val.value : val) - 1
    const tabel = document.getElementById('myTable')
    Array.from(tabel.querySelectorAll('tbody tr')).sort((a, b) => {
        const nilai1 = a.getElementsByTagName('td')[index].innerText.toLowerCase()
        const nilai2 = b.getElementsByTagName('td')[index].innerText.toLowerCase()
        return nilai1.localeCompare(nilai2)
    }).forEach((val) => {
        val.parentElement.appendChild(val)
    })
}