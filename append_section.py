import re
import os

file_path = r"c:\Users\Murilo vieira\Documents\projetos\site teste 2\src\pages\blog\teste2.astro"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

html_to_append = """
<section>
  <h2>Como a bicicleta Rava aro 29 se compara com outras marcas populares?</h2>
  <p>
    Se as limitações de um modelo de entrada como a Rava aro 29 já não te atendem, o mercado oferece máquinas com um refinamento que muda o seu pedal da água para o vinho. É importante entender como ela se posiciona perante outras opções para decidir o melhor investimento.
  </p>
  <ul>
    <li><strong>Rava Pressure</strong>: Freio a Disco Hidráulico, 20V, Foco: Trilhas e Trajetos Urbanos</li>
    <li><strong>Caloi Moab</strong>: Freio Hidráulico (Óleo), 18V Microshift, Foco: Trilha Leve / Misto</li>
    <li><strong>Absolute Nero 4</strong>: Freio Hidráulico (Óleo), 1x12V, Foco: Performance / Subidas Duras</li>
  </ul>
  
  <h3>Rava vs Caloi</h3>
  <p><strong>Caloi Bicicleta Moab Aro 29 (18 Vel. Microshift)</strong><br/>⭐ A Confiança da Marca Clássica para Uso Misto</p>
  <p>
    Enquanto a Rava foca no custo-benefício para iniciantes, a Caloi Moab redefine o conceito de mountain bike de entrada porque prioriza uma integridade estrutural mais avançada, e não apenas uma pintura bonita. O grande diferencial que destaco na Caloi em relação à Rava é a transmissão Microshift de 18 velocidades.
  </p>
  <p><strong>O que isso muda?</strong><br/>
    Diferente de sistemas comuns que vivem "cruzando" a corrente, as 18 marchas da Moab entregam as opções exatas que você precisa, acumulando menos sujeira e exigindo menos regulagem na oficina do que alguns conjuntos de 20 marchas. Os freios a disco hidráulicos Logan da Caloi também são maravilhosos, com uma modulação levíssima. Você sente o controle total na ponta do dedo indicador, sem fazer força. É um equipamento que respeita o seu esforço, ideal para estradões de terra e asfalto com buracos.
  </p>
  <p><strong>Peso-Pesado: Caloi Bicicleta Moab Aro 29</strong><br/>
    Estrutura robusta em alumínio e 18 marchas Microshift para quem busca durabilidade superior em trilhas intermediárias.
  </p>
  <ul>
    <li>Quadro em alumínio resistente</li>
    <li>Geometria versátil</li>
    <li>Câmbios Microshift</li>
  </ul>
  <p><a href="https://meli.la/1gs3ipC" target="_blank">CLIQUE AQUI PARA VER O PREÇO</a></p>
  <p><strong>Prós</strong></p>
  <ul>
    <li>Transmissão Microshift de 18v com trocas fluidas e menos visita ao mecânico.</li>
    <li>Freios hidráulicos que não te deixam com dor na mão após uma descida longa.</li>
    <li>Quadro com soldas reforçadas para não trincar em impactos.</li>
    <li>Rede de assistência gigantesca da Caloi.</li>
  </ul>
  <p><strong>Contras</strong></p>
  <ul>
    <li>O quadro mais robusto eleva o peso, exigindo perna nas ladeiras brutas (comparado ao quadro leve da Rava).</li>
    <li>Pneus originais rodam rápido no asfalto, mas derrapam em lama espessa.</li>
  </ul>

  <h3>Rava vs Absolute Nero 4</h3>
  <p><strong>Bicicleta Aro 29 Absolute Nero 4 (1x12 Hidráulico)</strong><br/>⛰️ Para Engolir Subidas e Trilhas Técnicas</p>
  <p>
    Se a Rava te introduziu ao ciclismo, mas você já quer colocar a bike na terra de verdade, a Absolute Nero 4 é um divisor de águas absoluto. O pulo do gato investigativo aqui é a transmissão 1x12. Ao usar uma única coroa na frente, você elimina o câmbio dianteiro que geralmente vem na Rava e outras bikes de entrada.
  </p>
  <p><strong>O resultado?</strong><br/>
    Você tira quase um quilo de peso da bicicleta, ganha um guidão muito mais limpo e encerra de vez o pesadelo da corrente caindo ao mudar de marcha numa subida! A marcha traseira mais leve é gigantesca, funcionando como um guincho que te ajuda a escalar barrancos. Os freios hidráulicos complementam a agressividade dela em descidas. A única ressalva: atenção redobrada ao tamanho do quadro (geralmente focado em 15"), faça as contas do seu Bike Fit para ter certeza de que o conforto será perfeito, algo que as geometrias mais tradicionais da Rava costumam facilitar.
  </p>
  <p><strong>Peso-Pesado: Bicicleta Aro 29 Absolute Nero 4</strong><br/>
    Para quem quer encarar Trilhas Pesadas com transmissão 1x12.
  </p>
  <ul>
    <li>Transmissão 1x12</li>
    <li>Freios hidráulicos</li>
    <li>Suspensão com trava</li>
  </ul>
  <p><a href="https://meli.la/2FkqvES" target="_blank">CLIQUE AQUI PARA VER O PREÇO</a></p>
  <p><strong>Prós</strong></p>
  <ul>
    <li>Transmissão 1x12 super moderna que facilita muito as subidas duras.</li>
    <li>Freios hidráulicos que entregam confiança total no controle.</li>
    <li>Cabeamento interno que esconde os fios, deixando a bike linda e protegida da lama.</li>
    <li>Peso total altamente competitivo.</li>
  </ul>
  <p><strong>Contras</strong></p>
  <ul>
    <li>Exige muita atenção à tabela de tamanhos antes de comprar.</li>
    <li>O selim original tem pegada esportiva; se você não usa bermuda de ciclismo acolchoada, pode sentir dor nos primeiros dias.</li>
  </ul>
</section>
"""

end_match = re.search(r'</div>\s*<aside className="article-sidebar">', content)
if end_match:
    end_idx = end_match.start()
    new_content = content[:end_idx] + html_to_append + "\n" + content[end_idx:]
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Updated successfully")
else:
    print("Could not find insertion point")
