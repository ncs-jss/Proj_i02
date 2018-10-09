var item1="Item_One"; //temporary
var item2="Item_Two"; //temporary
var mylist = [
    {name: 'Item_One', age: 42},
    {name: 'Item_Two', age: 18},
    ]

function addItem(curState)
            {
                var valueI=1;                
                document.getElementById("itemList").innerHTML="<tr id='tr"+valueI+"'><td id='item_name"+valueI+"'>"+item1+"</td><td id='item_qty"+valueI+"'><button class='minus-btn' type='button' name='button' value='1'><i class='material-icons'>remove</i></button><input id='quantity' type='text' name='"+item1+"' value='0'><button class='plus-btn' type='button' name='button' value='1'><i class='material-icons'>add</i></button></td></tr>"



                $('.minus-btn').on('click', function(e) {
                    e.preventDefault();
                    var $this = $(this);
                    var $input = $this.closest('td').find('input');
                    var value = parseInt($input.val());
                    if (value >= 1) 
                    {
                        value = value - 1;
                    } 
                    else 
                    {
                        value = 0;
                    }
                    $input.val(value);
                    if ($('#cartitem'+this.value).length)
                    {
                        $('#cartitem'+this.value).html(item1);
                        $('#cartitemqty'+this.value).html(value);
                    }
                    else
                    {
                        $( "#item_cart" ).append('<tr><td id="cartitem'+this.value+'">'+item1+'</td><td id="cartitemqty'+this.value+'">'+value+'</td></tr>');
                    }
                    
                });
                $('.plus-btn').on('click', function(e) {
                    e.preventDefault();
                    var $this = $(this);
                    var $input = $this.closest('td').find('input');
                    var value = parseInt($input.val());
                    if (value < 100) 
                    {
                        value = value + 1;
                    } 
                    else 
                    {
                        value =100;
                    }
                    $input.val(value);
                    if ($('#cartitem'+this.value).length)
                    {
                        $('#cartitem'+this.value).html(item1);
                        $('#cartitemqty'+this.value).html(value);
                    }
                    else
                    {
                        $( "#item_cart" ).append('<tr><td id="cartitem'+this.value+'">'+item1+'</td><td id="cartitemqty'+this.value+'">'+value+'</td></tr>');
                    }
                });
                }

function submitform() {
var mytitle = document.getElementById("title").value;
var mydetail = document.getElementById("detail").value;
var childObj = document.getElementById('itemList');
var finalItems= [[]];
for (var i = 0; i < childObj.childNodes.length; i++)
{   
    var childchild = document.getElementById(childObj.childNodes[i].id);
    var finalChild = document.getElementById(childchild.childNodes[1].id);
    finalChild.childNodes[1].name;   
    finalItems[i][0]=finalChild.childNodes[1].name;
    finalItems[i][1]=finalChild.childNodes[1].value;  
}
var myObj = {title: mytitle , detail: mydetail, id: finalItems };
//FORMDATA
var formData = JSON.stringify(myObj);
}
$(document).ready(function() {
    $('select').material_select();
});

