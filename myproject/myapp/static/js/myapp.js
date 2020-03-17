document.getElementById('menu').addEventListener ('click' ,
 function(){
  document.getElementById('menu').style.display='none';
  document.getElementById('newmenu').style.display='inline';
  document.getElementById('dropdown').style.display= 'flex';
  document.getElementById('postsvg').style.display= 'flex'});

document.getElementById('newmenu').addEventListener ('click' ,
 function(){
  document.getElementById('newmenu').style.display='none';
  document.getElementById('menu').style.display='inline';
  document.getElementById('dropdown').style.display= 'none';
  document.getElementById('postsvg').style.display= 'none'});
