$('#type-search-form').hide();
$('#name-search-form').hide();

$("#name_button").click(function(event) {
 $("#name-search-form").show();
 $("#type-search-form").hide();
 });

 $("#type_button").click(function(event) {
  $("#type-search-form").show();
  $("#name-search-form").hide();
  });

//
// $('input[type="radio" id="by_name"]').change(function() {
//   if ($('input[name="by_name"]:checked')) {
//     $("#name-search-form").show();
//   }
// });
//
//

//
// $('input[type="radio" id="by_type"]').change(function() {
//   if ($('input[name="by_type"]:checked')) {
//     $("#type-search-form").show();
//   }
// });
