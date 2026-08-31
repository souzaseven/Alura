/*
 * Classificando desempenho acadêmico
 * Desafio do curso de Pensamento Computacional (Alura).
 *
 * Recebe a média final do estudante e exibe uma mensagem de acordo
 * com a regra pedagógica, usando estruturas condicionais encadeadas.
 */

const readline = require("readline");

function classificar(media) {
  if (media < 5.0) {
    return "Você está reprovado.";
  } else if (media < 7.0) {
    return "Você está de recuperação.";
  } else {
    return "Parabéns! Você foi aprovado.";
  }
}

function lerMedia() {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  const perguntar = () => {
    rl.question("Informe a média final do estudante (0 a 10): ", (entrada) => {
      const media = Number(entrada.replace(",", "."));

      if (Number.isNaN(media)) {
        console.log("Valor inválido. Digite um número, por exemplo: 7,5");
        return perguntar();
      }
      if (media < 0 || media > 10) {
        console.log("Média inválida. Informe um valor entre 0 e 10.");
        return perguntar();
      }

      console.log(classificar(media));
      rl.close();
    });
  };

  perguntar();
}

lerMedia();
