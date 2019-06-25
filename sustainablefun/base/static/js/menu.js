$(document).ready(function () {

    /**
     * Implementação do Hover persistente no menu, ou seja, o sublinhado persiste sobre a página atual
     * e não somente enquanto estou com o mouse em cima do item do menu.
     *
     * @param element_id
     * @returns {*|jQuery|void}
     */
    const persistirHover = element_id => $(element_id).toggleClass('PAGINA_ATUAL');

    /**
     * Implementação do clareamento do texto persistente sobre o texto do item do menu referente a página atual
     * @param element_id
     * @returns {*|jQuery|void}
     */
    const persistirHoverTexto = element_id => $(element_id).toggleClass('PAGINA_ATUAL_TEXTO');

    /**
     * Verificação da página atual e transformações necessárias no menu para o item referente a mesma.
     */
    switch (window.location.pathname) {
        case '/':
            persistirHover('#home_li');
            persistirHoverTexto('#home_a');
            break;
        case '/aboutus':
            persistirHover('#aboutus_li');
            persistirHoverTexto('#aboutus_a');
            break;
        case '/workshops':
            persistirHover('#workshops_li');
            persistirHoverTexto('#workshops_a');
            break;
    }

});
