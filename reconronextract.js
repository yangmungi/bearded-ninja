var weeks = [];

for (var i in tds) { 
    if (i % 20 == 0) {
        continue;
    }
    
    var kNode = tds[i]; 

    if (i > 140) {
        i = i - 140;
    }

    if (weeks[i] == undefined) {
        weeks[i] = [];
    }


    if (kNode.children != undefined && kNode.children.length > 1) {
        it = kNode.children[1].innerText;
        weeks[i].push(it);
    }
}
