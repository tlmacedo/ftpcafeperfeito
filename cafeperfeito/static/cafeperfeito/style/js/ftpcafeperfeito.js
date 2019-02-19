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

// $(document).ready(function () {
//     $('.msk-data').mask('11/11/1111');
//     $('.msk-hora').mask('00:00:00');
//     $('.msk-data_hora').mask('00/00/0000 00:00:00');
//     $('.msk-cep').mask('00000-000');
//     $('.msk-telefone').mask('9 0000-0000');
//     $('.msk-telefone_com_ddd').mask('(00) 0000-0000');
//     $('.msk-phone_us').mask('(000) 000-0000');
//     $('.msk-mixed').mask('AAA 000-S0S');
//     $('.msk-ncm').mask('00.0000.00');
//     $('.msk-cest').mask('00.000.00');
//     $('.msk-cnpj').mask('00.000.000/0000-00', {reverse: true});
//     $('.msk-cpf').mask('000.000.000-00', {reverse: true});
//     $('.msk-money').mask('000.000.000.000.000,00', {reverse: true});
// });

// $('#codigo').mask('AA/SS/YYYY', {
//     'translation': {
//         A: {pattern: /[A-Z]/},
//         S: {pattern: /[a-z]/},
//         Y: {pattern: /[0-9]/},
//     }
// });

$(document).ready(function () {
    $('.numero').mask('000000000000000000000000000000')
    $('.date').mask('00/00/0000');
    $('.time').mask('00:00:00');
    $('.date_time').mask('00/00/0000 00:00:00');
    $('.cep').mask('00000-000');
    $('.phone').mask('0000-0000');
    $('.phone_with_ddd').mask('(00) 0000-0000');
    $('.phone_us').mask('(000) 000-0000');
    $('.mixed').mask('AAA 000-S0S');
    $('.cpf').mask('000.000.000-00', {reverse: true});
    $('.cnpj').mask('00.000.000/0000-00', {reverse: true});
    $('.money').mask('000.000.000.000.000,00', {reverse: true});
    $('.money2').mask("#.##0,00", {reverse: true});
    $('.peso3').mask("#.##0,000", {reverse: true});
    $('.ip_address').mask('0ZZ.0ZZ.0ZZ.0ZZ', {
        translation: {
            'Z': {
                pattern: /[0-9]/, optional: true
            }
        }
    });
    $('.ip_address').mask('099.099.099.099');
    $('.percent').mask('##0,00%', {reverse: true});
    $('.clear-if-not-match').mask("00/00/0000", {clearIfNotMatch: true});
    $('.placeholder').mask("00/00/0000", {placeholder: "__/__/____"});
    $('.fallback').mask("00r00r0000", {
        translation: {
            'r': {
                pattern: /[\/]/,
                fallback: '/'
            },
            placeholder: "__/__/____"
        }
    });
    $('.selectonfocus').mask("00/00/0000", {selectOnFocus: true});
});


// var SPMaskBehavior = function (val) {
//         return val.replace(/\D/g, '').length === 9 ? '0 0000-0000' : '9 0000-0000';
//     },
//     spOptions = {
//         onKeyPress: function (val, e, field, options) {
//             field.mask(SPMaskBehavior.apply({}, arguments), options);
//         }
//     };
//
// $('.sp_celphones').mask(SPMaskBehavior, spOptions);