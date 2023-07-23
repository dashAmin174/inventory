function print(page){
  let product_name = $(".PRODUCT_NAME").val();
  let product_code = $(".PRODUCT_CODE").val();
  let product_color = $(".PRODUCT_COLOR").val();
  let product_location = $(".PRODUCT_LOCATION").val();
  let product_hall = $(".PRODUCT_HALL").val();
  let product_unit = $(".PRODUCT_UNIT").val();
  let jpub = $(".PRODUCT_DATE").val();
  let printContents = $('<div>').addClass('cardex').append(
    $('<div>').addClass('h-cardex').append(
      $('<span>').text(`نام کالا : ${product_name}`),
      $('<span>').text(`کد کالا : ${product_code}`),
      $('<span>').text(`رنگ کالا : ${product_color}`),
      $('<span>').text(`نام انبار : ${product_location}`),
      $('<span>').text(`محل کالا : ${product_hall}`),
      $('<span>').text(`واحد شمارش : ${product_unit}`),
      $('<span>').text(`تاریخ ثبت : ${jpub}`),
      $('<hr>'),
      $('table').addClass(`table`).append(
        $('thead').addClass(`table-dark`).append(
          $('tr').append(
            $('th').text(`ردیف`),
            $('th').text(`تاریخ`),
            $('th').text(`شماره فاکتور`),
            $('th').text(`شرح اقدامات`),
            $('th').text(`ورودی`),
            $('th').text(`خروجی`),
            $('th').text(`موجودی`),
            $('th').text(`اقدام کننده`),
          )
        )
      )
    )
  );
  
  var printWin = window.open('', '', 'width=1000,height=1000');
  printWin.document.write('<html dir="rtl"><head><title>${page} Cardex</title>');
  printWin.document.write('</head><body >');
  printWin.document.write(printContents);
  printWin.document.write('</body></html>');
  printWin.document.close();
  printWin.print();
  }// End function print
$(".do1").click(function() {
  let productCode = $("input[name='CODE']").val();
  let factorNumber = $("input[placeholder='شماره حواله / فاکتور']").val();
  let number = $("input[placeholder='تعداد']").val();
  let description = $("input[placeholder='شرح اقدامات']").val();
  let operation = $("select:eq(0)").find(":selected").text();
  let data = {
      'product_code' : productCode,
      'factor_number' : factorNumber,
      'number' : number,
      'description' : description,
      'operation' : operation,
  };
  $.ajax({
      url : '/inventory/js_update_products',
      type : 'POST',
      data : data,
      success: function(response) {
          if (response.success === false) {
            Swal.fire({
              icon: "error",
              title: response.status,
              showConfirmButton: false,
              timer: 3000,
            });
          } else {
            Swal.fire({
              icon: "success",
              title: response.status,
              showConfirmButton: false,
              timer: 2000,
            });
            location.reload(true)
          }
        },
        error: function(xhr, status, error) {
          console.log(status);
          Swal.fire({
            icon: "error",
            title: status,
            showConfirmButton: false,
            timer: 3000,
          });
        }
  });//End ajax
});// End btn do1