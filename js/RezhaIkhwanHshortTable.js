
// v1.0.0
//cara pake nya pangil olclic di html bagia th dan beri index th ke berapa dimulai dari 1
// contoh
//<table id="myTable">
{/* <thead>
    <tr>
        <th onclick="sort(1)">nama</th>
        <th onclick="sort(2)">tanggal</th>
        <th onclick="sort(3)">waktu</th>
        <th onclick="sort(4)">lokasi</th>
    </tr>
// </thead> */}

function sort(val) {
    const index = (isNaN(val) ? val.value : val) - 1
    const tabel = document.getElementById('myTableShort')
    Array.from(tabel.querySelectorAll('tbody tr')).sort((a, b) => {
        const nilai1 = a.getElementsByTagName('td')[index].innerText.toLowerCase()
        const nilai2 = b.getElementsByTagName('td')[index].innerText.toLowerCase()
        return nilai1.localeCompare(nilai2)
    }).forEach((val) => {
        val.parentElement.appendChild(val)
    })
}
//v 2.0.0
// hanya tambah class  "myTableShort" di table contoh:
{/* <table id = "myTable" >
      <thead>
    
      </thead>
      <tbody>

      </tbody>
    </table > */}
const myTableTh = document.getElementById("myTableShort").querySelectorAll("thead th");
myTableTh.forEach((element, i) => {
    element.addEventListener("click", e => {
        sort(i + 1)
    })
});