async function logJSONData(link) {
    const response = await fetch(link);
    const jsonData = await response.json();
    jsonData.map((ev)=>{
        console.log(ev);
        rowdata = addData(ev.id,ev.name_lap,ev.brand_name,ev.price,ev.original_price,ev.seller_id)
        document.querySelector('#tabledata > tbody').appendChild(rowdata)
    })
}

logJSONData("http://localhost:8002/datalist/")
function addData(vl1,vl2,vl3,vl4,vl5,vl6){
    const column = document.createElement("tr")
    const row1 = document.createElement("td")
    row1.innerHTML =vl1
    column.appendChild(row1)
    const row2 = document.createElement("td")
    row2.innerHTML =vl2
    column.appendChild(row2)
    const row3 = document.createElement("td")
    row3.innerHTML =vl3
    column.appendChild(row3)
    const row4 = document.createElement("td")
    row4.innerHTML =vl4
    column.appendChild(row4)
    const row5 = document.createElement("td")
    row5.innerHTML =vl5
    column.appendChild(row5)
    const row6 = document.createElement("td")
    row6.innerHTML =vl6
    column.appendChild(row6)
    return column
}

document.getElementById("button_tim").onclick = ()=>{
    const ten = document.querySelector("input#ten").value
    const loai = document.querySelector("input#loai").value
    const giamin = document.querySelector("input#giamin").value
    const giamax = document.querySelector("input#giamax").value
    if (ten=="" && loai=="" &&  giamin=="" &&  giamax=="" ){
        alert("Chưa nhập xong")
        return
    }
    let link = "http://localhost:8002/filterdata/?"
    if (ten!=""){
        link+="name_lap="+ten+"&"
    }
    if (loai!=""){
        link+="brand_name="+loai+"&"
    }
    if (giamin!=""){
        link+="price_min="+giamin+"&"
    }
    if (giamax!=""){
        link+="price_max="+giamax+"&"
    }
    link=link.substring(0,link.length-1)
    document.querySelector('#tabledata > tbody').innerHTML("")
    logJSONData(link)
}


