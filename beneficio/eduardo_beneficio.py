"""
memory game
criação das cartas
imagem e combinações das cartas
funções de desativação das cartas já combinadas
embaralho das cartas com duplas
😎👌
"""

#@charset "utf-8"; /* Define a codificação de caracteres para CSS*/

#/* --- reset básico e configurações iniciais ---*/

{
    #box-sizing: border-box; /* Garante que padding (espaçamento interno) e border (borda) sejam 
    #incluidos na largura/altura total de um elemento, evitando surpresas no layout */

#margin: 0; /*remove margens padrão de todos os elementos*/
#padding: 0; /* Remove preenchimentos padrão de todos os elementos */


}

body{
    #font-family: ´Arial´, sans-serif; /* Define a fonte principal para todo o texto */
    #display: flex; /* Usa Flexbox para organizar o conteúdo */
    #flex-direction: column; /* Organiza os itens em uma coluna (ótimo para mobile)
    #justify-content: flex-start; /* Alinha o conteúdo ao topo em telas pequenas */
    #align-items: center; /* Centraliza o conteúdo horizontalmente */
}