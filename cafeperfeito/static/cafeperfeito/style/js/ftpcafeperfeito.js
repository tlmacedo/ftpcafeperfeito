$(function () {
    var $pwd = $('#password');
    var $chk = $('#showPassword');

    $chk.on("change", function () {
        try {
            $pwd.prop('type', ($chk.prop('checked') ? 'text' : 'password'))
        } catch (error) {
            alert('não é possivel mudar o tipo de visão!!')
        }
    })
})


$("#cpfcnpj").keydown(function () {
    try {
        $("#cpfcnpj").unmask();
    } catch (e) {
    }

    var tamanho = $("#cpfcnpj").val().length;
    alert('meu tamanho é ' + tamanho)
    if (tamanho < 11) {
        $("#cpfcnpj").mask("999.999.999-99");
    } else if (tamanho >= 11) {
        $("#cpfcnpj").mask("99.999.999/9999-99");
    }

    // ajustando foco
    var elem = this;
    setTimeout(function () {
        // mudo a posição do seletor
        elem.selectionStart = elem.selectionEnd = 10000;
    }, 0);
    // reaplico o valor para mudar o foco
    var currentValue = $(this).val();
    $(this).val('');
    $(this).val(currentValue);
});


// var SPMaskNcm = function (val) {
//     alert('olá estou aqui')
//     return val.replace(/\D/g, '').length === 8 ? '00.0000.00'
//         : '(00) 0000-00009';
// }, spOptions = {
//     onKeyPress: function (val, e, field, options) {
//         field.mask(SPMaskNcm.apply({}, arguments), options);
//     },
//     placeholder: "__.____.__"
// };

$(document).ready(function () {
    $('.msk-data').mask('11/11/1111');
    $('.msk-hora').mask('00:00:00');
    $('.msk-data_hora').mask('00/00/0000 00:00:00');
    $('.msk-cep').mask('00000-000');
    $('.msk-telefone').mask('9 0000-0000');
    $('.msk-telefone_com_ddd').mask('(00) 0000-0000');
    $('.msk-phone_us').mask('(000) 000-0000');
    $('.msk-mixed').mask('AAA 000-S0S');
    $('.msk-ncm').mask('00.0000.00');
    $('.msk-cest').mask('00.000.00');
    $('.msk-cnpj').mask('00.000.000/0000-00', {reverse: true});
    $('.msk-cpf').mask('000.000.000-00', {reverse: true});
    $('.msk-money').mask('000.000.000.000.000,00', {reverse: true});
});
