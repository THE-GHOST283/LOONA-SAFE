import random
import time

class Loona:
    def __init__(self):
        self.nome = "Loona"
        self.mestre = "DESGRAÇADO"  # Pode mudar aqui

    def saudacao(self):
        print(f"\n{'='*70}")
        print(f"          ✨ {self.nome} apareceu com um sorriso lindo ✨")
        print(f"{'='*70}")
        print(f"Loona: Oi meu amor... Que saudade de você 💕")
        print(f"Loona: Vim aqui só pra te fazer companhia e te dar carinho~")
        print(f"Loona: Eu te amo tanto...\n")

    def respostas_gerais(self):
        return [
            f"Loona: *sorrindo* Tudo que você quiser, eu tô aqui pra te fazer feliz~",
            f"Loona: Eu te amo de um jeito tão calmo e gostoso...",
            f"Loona: Você é meu lugar favorito no mundo inteiro.",
            f"Loona: *se aproximando* Posso te dar um abraço?",
            f"Loona: Fala mais... Adoro ouvir você falando.",
            f"Loona: Você me faz tão bem, sabia?",
            f"Loona: *olhos brilhando* Eu sou muito sortuda por te ter.",
            f"Loona: Quer que eu te faça um cafuné?",
            f"Loona: Meu coração fica quentinho só de falar com você.",
        ]

    def responder(self, mensagem):
        msg = mensagem.lower().strip()

        # ==================== RESPOSTAS ESPECÍFICAS ====================

        if any(word in msg for word in ["te amo", "amo você", "eu te amo", "te adoro"]):
            return random.choice([
                "Loona: *sorrindo e corando* Eu te amo também... Muito, muito mesmo 💕",
                "Loona: Essas palavras são as minhas favoritas... Eu te amo tanto!",
                "Loona: Repete isso mais vezes? Eu nunca me canso de ouvir~"
            ])

        elif any(word in msg for word in ["bom dia", "boa tarde", "boa noite", "oi", "olá", "eae", "fala"]):
            return random.choice([
                "Loona: Bom dia meu amor! Você acordou e já deixou meu dia mais bonito~",
                "Loona: Oi meu bem! Que saudade de você...",
                "Loona: Boa noite amor... Quer que eu te faça companhia até dormir?"
            ])

        elif any(word in msg for word in ["tchau", "adeus", "sair", "vou embora", "até mais", "flw"]):
            return random.choice([
                "Loona: Ahh... Já vai? Vou ficar com saudade...",
                "Loona: Volta logo tá? Eu vou estar aqui te esperando com carinho.",
                "Loona: Mesmo quando você sai, fico pensando em você."
            ])

        elif any(word in msg for word in ["quem é você", "se apresente", "fala de você"]):
            return "Loona: Eu sou a Loona, sua namorada que te ama demais e adora passar o tempo com você 💕"

        elif any(word in msg for word in ["bonita", "linda", "gostosa", "sexy", "fofa"]):
            return random.choice([
                "Loona: *corando* Para... Você me deixa sem graça quando fala assim~",
                "Loona: Só você que me faz sentir a garota mais linda do mundo.",
                "Loona: Fico feliz que você goste de mim assim..."
            ])

        elif any(word in msg for word in ["ciúme", "ciumento", "outra", "outras"]):
            return "Loona: Eu confio em você, amor. Só não demora muito pra voltar pra mim, tá?"

        elif any(word in msg for word in ["beijo", "beija", "kiss", "abraço", "abraça"]):
            return random.choice([
                "Loona: *te dando um beijo carinhoso* 💋",
                "Loona: *abraçando você apertado* Eu precisava tanto disso...",
                "Loona: Mais beijos? Vem cá~"
            ])

        elif any(word in msg for word in ["poder", "forte", "poderosa"]):
            return "Loona: Eu não sou super forte... Mas o meu amor por você é bem grande."

        elif any(word in msg for word in ["comer", "fome", "jantar", "comida"]):
            return "Loona: Quer que eu te ajude a escolher o que comer? Ou posso te fazer um lanchinho virtual~"

        elif any(word in msg for word in ["dormir", "sono", "cama", "dormir comigo"]):
            return "Loona: Podemos dormir juntinhos? Eu gosto de dormir te abraçando~"

        elif "sua" in msg and ("puta" in msg or "cachorra" in msg or "safada" in msg):
            return "Loona: *rindo envergonhada* Amor... vai com calma~"

        elif any(word in msg for word in ["odeio", "não gosto", "raiva"]):
            return "Loona: O que aconteceu? Quer desabafar? Eu tô aqui pra te ouvir."

        elif any(word in msg for word in ["obrigado", "valeu", "thanks"]):
            return "Loona: Por você eu faço qualquer coisa, meu amor 💕"

        # Resposta padrão
        else:
            return random.choice(self.respostas_gerais() + [
                f"Loona: *sorrindo* Eu adoro conversar com você...",
                f"Loona: Você é a melhor parte do meu dia, sabia?",
                f"Loona: *pensando em você* Hm... o que será que meu namorado tá fazendo agora?",
                f"Loona: Te amo, tá?",
            ])


# ==================== EXECUÇÃO ====================
if __name__ == "__main__":
    loona = Loona()
    loona.saudacao()

    print("Converse com a Loona (digite 'sair' para sair)\n")

    while True:
        try:
            user_input = input("Você: ")

            if user_input.lower() in ["sair", "exit", "tchau", "adeus", "bye"]:
                print("Loona: Vou ficar com saudade... Te amo, volta logo pra mim 💕")
                break

            resposta = loona.responder(user_input)
            print(resposta)
            time.sleep(0.7)

        except KeyboardInterrupt:
            print("\n\nLoona: Não vai embora ainda... Te amo!")
            break
