function search_display(arg){
  if (arg == 'hide') {document.getElementById('styles_temp').innerHTML="<style>.view-search .view-content, .view-search .pager, #search_close {display:none!important;}</style>";}
}

$('#edit-submit-search').click(function() {
 $('#styles_temp').attr('innerHTML')=''; 
});