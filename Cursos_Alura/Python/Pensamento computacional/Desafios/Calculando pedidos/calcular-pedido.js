/*
 * Calculando pedidos
 * Desafio do curso de Pensamento Computacional (Alura).
 *
 * Calcula o valor total de um pedido de lanchonete a partir das quantidades
 * de hambúrgueres, batatas fritas e refrigerantes informadas pelo cliente.
 */

const readline = require("readline");

const PRECO_HAMBURGUER = 12.0;
const PRECO_BATATA = 7.0;
const PRECO_REFRI = 5.0;

function calcularTotal(qtdHamburguer, qtdBatata, qtdRefri) {
  const totalHamburguer = qtdHamburguer * PRECO_HAMBURGUER;
  const totalBatata = qtdBatata * PRECO_BATATA;
  const totalRefri = qtdRefri * PRECO_REFRI;
  return totalHamburguer + totalBatata + totalRefri;
}

function main() {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  const perguntas = [
    "Quantidade de hambúrgueres: ",
    "Quantidade de batatas fritas: ",
    "Quantidade de refrigerantes: ",
  ];
  const quantidades = [];

  const perguntar = () => {
    if (quantidades.length === perguntas.length) {
      const [qtdHamburguer, qtdBatata, qtdRefri] = quantidades;
      const totalPedido = calcularTotal(qtdHamburguer, qtdBatata, qtdRefri);
      console.log(`Valor total do pedido: R$ ${totalPedido.toFixed(2)}`);
      rl.close();
      return;
    }

    rl.question(perguntas[quantidades.length], (entrada) => {
      const quantidade = Number(entrada);

      if (!Number.isInteger(quantidade) || quantidade < 0) {
        console.log(
          "Valor inválido. Digite um número inteiro não negativo (ex.: 2)."
        );
        return perguntar();
      }

      quantidades.push(quantidade);
      perguntar();
    });
  };

  perguntar();
}

main();
