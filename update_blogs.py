import os

def replace_content(filepath, new_content, title, description):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    start_str = '---\n\n<Layout'
    start_idx = content.find(start_str)
    
    end_str = '\n      <aside className="article-sidebar">'
    end_idx = content.find(end_str)
    
    if start_idx == -1 or end_idx == -1:
        print(f"Could not find bounds in {filepath}")
        return
        
    frontmatter = content[:start_idx].split('---')[1]
    
    final_content = f"""---
import Layout from '../../layouts/Layout.astro';
import Navbar from '../../components/Navbar';

const title = "{title}";
const description = "{description}";
---

<Layout title={{title}} description={{description}}>
  <Navbar client:load />

  <article className="article-page">
    <header className="article-header">
      <div className="container">
        <div className="meta animate-fade">
          <span className="category">Montagem</span>
          <span className="dot">•</span>
          <span className="date">10 Set 2026</span>
        </div>
        <h1 className="animate-fade" style="animation-delay: 0.1s">{{title}}</h1>
        <p className="lead animate-fade" style="animation-delay: 0.2s">
          {{description}}
        </p>
      </div>
    </header>

    <div className="container article-container">
      <div className="article-content">

{new_content}
""" + content[end_idx:]
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(final_content)

content_teste1 = """<p>
  Este artigo detalha o processo completo para montar uma bicicleta aro 29, desde a organização das peças até a regulagem final dos componentes. A montagem foi realizada em uma bicicleta de qualidade média, com peças boas, o que garante um bom equilíbrio entre desempenho e custo. Além disso, abordaremos algumas particularidades do processo, como a adaptação de componentes específicos para este tamanho de aro e as melhores práticas para otimizar a segurança e o conforto do ciclista. Seguindo esse guia, você poderá montar sua própria bicicleta com confiança, ajustando cada etapa para garantir uma experiência de pedalada eficiente e prazerosa.
</p>

<section>
  <h2>Organização Inicial e Preparação das Peças</h2>
  <p>
    Antes de iniciar a montagem, é fundamental preparar e organizar todas as peças com cuidado para evitar confusão durante o processo. Essa etapa previne atrasos e erros, garantindo que cada componente esteja pronto para ser utilizado no momento certo. Separe as peças por tipo, tamanho e função, criando um espaço de trabalho ordenado que facilite o acesso rápido a cada item. Verifique se todas as peças estão em perfeito estado, sem defeitos ou danos que possam comprometer o resultado final. Além disso, ter todas as ferramentas necessárias à mão contribui para a agilidade e eficiência do trabalho. Assim, o processo flui de maneira contínua e segura, reduzindo retrabalhos e aumentando a qualidade da montagem.
  </p>

  <h3>Passos para organização:</h3>
  <ul>
    <li>Retire cuidadosamente as peças da caixa principal e da caixa de acessórios, evitando qualquer dano durante o manuseio.</li>
    <li>Faça uma conferência detalhada para garantir que todas as peças listadas estejam presentes e em perfeito estado.</li>
    <li>Organize os componentes sobre a mesa, distribuindo-os de forma prática para facilitar a montagem:
      <ul>
        <li>Agrupe o canote e o banco juntos, pois são partes interligadas do assento.</li>
        <li>Posicione as câmeras ao lado, para acesso rápido durante a instalação.</li>
        <li>Mantenha os pedais separados na lateral, garantindo que não se percam ou se misturem com outras peças menores.</li>
        <li>Separe o suporte para garrafinha em área própria, facilitando a fixação.</li>
        <li>Organize os eixos e as forquetas lado a lado, para alinhar corretamente as estruturas frontais.</li>
      </ul>
    </li>
    <li>Abra cuidadosamente e descarte todas as embalagens plásticas e de papelão, para liberar espaço, evitar acúmulo de lixo e facilitar o manuseio das peças durante as próximas etapas.</li>
  </ul>
</section>

<section>
  <h2>Montagem do Quadro e Instalação Inicial</h2>
  <p>
    A montagem do quadro deve ser realizada com atenção especial à estrutura e alinhamento das peças, garantindo que todas as componentes estejam firmes e niveladas. Comece verificando se os perfis, suportes e parafusos são compatíveis entre si e com o projeto previamente definido. Utilize ferramentas apropriadas, como chaves de fenda, níveis e esquadros, para assegurar que o quadro esteja corretamente posicionado. Durante a instalação inicial, é fundamental fixar o quadro na parede ou base de forma segura, levando em conta o tipo de superfície e peso da estrutura. Certifique-se de que os pontos de fixação estejam distribuídos uniformemente para evitar tensões desnecessárias. Após fixar o quadro, realize uma revisão geral para confirmar que não há folgas ou peças soltas, além de assegurar que o conjunto está pronto para a etapa seguinte, como a instalação dos componentes elétricos ou mecânicos que dependem dessa estrutura. Essa preparação inicial é crucial para o desempenho e durabilidade do sistema.
  </p>

  <h3>Colocação do canote e preparação do quadro</h3>
  <p>
    Utilize inicialmente um canote usado para evitar danos ao canote novo do cliente durante a montagem. Posicione o canote cuidadosamente no suporte do quadro, garantindo que esteja bem encaixado para evitar folgas ou desalinhamentos. Se o quadro for pesado ou volumoso, peça ajuda para levantá-lo e facilitar a montagem de forma segura, prevenindo acidentes e danos ao equipamento. Durante todo o processo, mantenha o certificado de garantia em local seguro, para assegurar que esteja disponível caso seja necessário para futuras revisões ou trocas. Essa preparação adequada é fundamental para garantir a estabilidade e o bom funcionamento do conjunto, facilitando as próximas etapas da instalação.
  </p>

  <h3>Remoção das forquetas (enforcagatos)</h3>
  <ul>
    <li>Com um alicate adequado, corte cuidadosamente as forquetas, conhecidas popularmente como enforcagatos, para liberar as rodas sem danificá-las.</li>
    <li>Comece pela roda dianteira, remova-a com atenção e reserve-a em um local seguro para evitar riscos ou sujeiras.</li>
    <li>Em seguida, repita o mesmo procedimento para a roda traseira, garantindo que todas as forquetas estejam completamente removidas.</li>
    <li>Para finalizar, retire as embalagens plásticas que envolvem os pneus, usando uma faca afiada para cortar os resíduos com cuidado, evitando qualquer dano à borracha dos pneus.</li>
    <li>Certifique-se de eliminar completamente os restos de plástico para não comprometer o funcionamento das rodas ou a montagem posterior.</li>
  </ul>
</section>

<section>
  <h2>Instalação do Guidão (Guidon)</h2>
  <p>
    A instalação do guidão é uma etapa fundamental para garantir conforto e segurança na pilotagem. Comece verificando se o tubo do garfo está limpo e livre de sujeira ou resíduos que possam comprometer a fixação. Posicione o guidão no canote, alinhando-o centralmente para evitar desalinhamentos que prejudiquem o controle da moto ou bicicleta. Em seguida, aperte os parafusos de fixação com o torque recomendado pelo fabricante, evitando excesso que possa danificar a peça ou folga que cause instabilidade.
  </p>
  <p>
    É importante conferir o posicionamento da manopla e dos controles, ajustando-os para facilitar o alcance e a ergonomia das mãos. Após a fixação, teste o movimento do guidão para garantir que ele não trave nem tenha folgas. Para maior segurança, realize uma verificação final dos aperto após os primeiros quilômetros. Esses cuidados asseguram uma instalação adequada, promovendo melhor desempenho e conforto na condução.
  </p>

  <h3>Passos para instalar o guidão</h3>
  <ul>
    <li>Utilize um kit de chaves Allen com tamanhos variados, incluindo 2, 3, 4, 5, 6 e 7 mm, para garantir que todas as partes do guidão possam ser ajustadas corretamente.</li>
    <li>Desaperte cuidadosamente os parafusos do suporte do guidão utilizando a chave Allen de 4 mm, evitando forçar para não danificar as roscas.</li>
    <li>Posicione o guidão na altura desejada e rosqueie os quatro parafusos de fixação de maneira cruzada, formando um "X". Rosqueie todos sem apertar completamente para permitir ajustes posteriores.</li>
    <li>Faça uma pré-fixação dos parafusos apenas para manter o guidão estável, facilitando a centralização e o alinhamento correto.</li>
    <li>Centralize o guidão de modo que ele fique alinhado com a direção da bicicleta e deixe o aperto final dos parafusos para ser realizado após a instalação da roda, garantindo segurança e estabilidade no conjunto.</li>
  </ul>
</section>

<section>
  <h2>Instalação dos Pedais</h2>
  <p>
    Para garantir a correta instalação dos pedais, primeiramente identifique o lado correto de cada pedal, pois eles possuem roscas diferentes. O pedal direito tem rosca padrão direita e deve ser fixado no lado correspondente da bicicleta, enquanto o pedal esquerdo possui rosca inversa para evitar que se solte durante o uso. Utilize uma chave específica para pedais ou uma chave inglesa ajustável para realizar a fixação. Ao posicionar o pedal, comece a rosqueá-lo manualmente para evitar danos na rosca, depois aperte com a ferramenta até ficar firme, mas sem excesso de força, para não danificar o equipamento. Certifique-se também de aplicar um pouco de graxa nas roscas antes da instalação, o que facilita futuras remoções e previne corrosão. Após a fixação, teste o giro dos pedais para garantir que estão instalados corretamente e funcionando de maneira suave, sem folgas ou travamentos.
  </p>

  <h3>Procedimento recomendado</h3>
  <p>
    Antes de iniciar a montagem dos pedais, aplique graxa em todas as roscas, mesmo que a bicicleta seja nova. Isso evita o desgaste precoce, facilita futuras remoções e garante um encaixe mais seguro. Ao posicionar os pedais, é fundamental observar os lados corretos: o pedal esquerdo (lado L) deve ser apertado no sentido anti-horário, enquanto o pedal direito (lado D) é apertado no sentido horário, evitando o risco de travamento ou danos. Utilize uma chave 15 para realizar o aperto final, garantindo que esteja firme o suficiente para não soltar durante o uso. Porém, cuidado para não exagerar na força e danificar as roscas ou o pedal. Após o aperto, remova o excesso de graxa que sobrou com um pano limpo, mantendo a área de fixação limpa e livre para um bom funcionamento.
  </p>
</section>

<section>
  <h2>Montagem e Instalação do Câmbio</h2>
  <p>
    A montagem do câmbio exige atenção e precisão para garantir o funcionamento eficiente da bicicleta. Inicialmente, é fundamental verificar se todas as peças estão em bom estado e compatíveis entre si, incluindo o câmbio dianteiro ou traseiro, cabos, guias e parafusos. Na instalação, posicione o câmbio no suporte adequado do quadro, respeitando o alinhamento e a altura recomendados pelo fabricante. Em seguida, ajuste o aperto do parafuso de fixação para evitar folgas que possam prejudicar a troca de marchas. É importante também instalar e esticar corretamente o cabo de comando, assegurando que o movimento do câmbio seja suave e preciso. Por fim, faça os ajustes finos, regulando as molas de tensão e os limites para evitar que a corrente escape dos dentes, garantindo uma troca de marchas segura e eficiente. Esse processo, quando realizado corretamente, melhora a performance e a durabilidade do câmbio, contribuindo para uma melhor experiência de pedalada.
  </p>

  <h3>Montagem do câmbio traseiro</h3>
  <ul>
    <li>Use a chave Allen 5 para fixar cuidadosamente o câmbio traseiro no quadro da bicicleta, garantindo que a peça de alumínio não seja danificada durante o processo. Pressione o parafuso suavemente e evite apertar excessivamente para não comprometer a integridade do componente.</li>
    <li>Encaixe o câmbio nos suportes apropriados localizados na parte traseira do quadro, certificando-se de que esteja alinhado corretamente para o bom funcionamento das marchas. Um encaixe preciso evita problemas no deslocamento da corrente.</li>
    <li>Caso o cabo do câmbio esteja muito longo, utilize um alicate ou ferramenta adequada para cortar o excesso, ajustando-o para um comprimento ideal que permita liberdade de movimento sem interferências. Faça o acabamento com uma presilha para evitar que o cabo desfie.</li>
  </ul>
</section>

<section>
  <h2>Montagem das Rodas e Pneus</h2>
  <p>
    A montagem das rodas e pneus exige atenção a detalhes essenciais para garantir segurança, desempenho e durabilidade. Primeiramente, é fundamental verificar se as rodas estão perfeitamente alinhadas e balanceadas, evitando vibrações que possam comprometer o conforto e a estabilidade do veículo. O encaixe dos pneus deve ser feito de forma correta, garantindo que a válvula esteja bem posicionada e que o pneu não apresente deformações ou danos visíveis.
  </p>
  <p>
    Além disso, o torque dos parafusos da roda deve seguir as especificações do fabricante para evitar afrouxamentos ou excesso de pressão, o que pode causar empenamentos. A calibragem dos pneus precisa ser ajustada conforme a carga e tipo de uso do veículo, sempre respeitando os limites indicados no manual. Inspecionar o estado das bordas da roda e verificar se o pneu está corretamente assentado são etapas indispensáveis para evitar vazamentos e garantir desempenho ideal em diferentes condições de pista e clima.
  </p>

  <h3>Preparação dos pneus e câmaras</h3>
  <p>
    Remova completamente os rótulos plásticos e quaisquer inscrições dos pneus para garantir melhor aderência e evitar que essas partes interfiram na montagem. Confira se a roda já possui fita antiderrapante; caso não tenha, utilize uma câmera velha cortada para criar essa proteção extra, evitando que a fita original se mova ou danifique. Antes de instalar a câmara, realize um leve pré-inflamento para evitar dobras e possíveis perfurações durante a montagem. Ao posicionar a roda de freio a disco, deixe o disco voltado para cima para reduzir o risco de empenamento, garantindo maior durabilidade e segurança. Por fim, inflar o pneu até, no máximo, 35 psi previne possíveis estouros e garante que a banda de rodagem mantenha sua profundidade adequada, oferecendo ao mesmo tempo um rodar confortável e seguro.
  </p>

  <h3>Fixação das rodas no quadro</h3>
  <p>
    Utilize as presilhas dos eixos, também chamadas de eixo de blocagem, para fixar as rodas nos locais adequados do quadro da bicicleta. Antes da instalação, é fundamental retirar as travas de segurança dos freios hidráulicos para evitar danos e garantir um encaixe correto. Posicione a presilha do eixo do freio do lado correspondente, de modo que não atrapalhe o funcionamento do câmbio, mantendo o alinhamento correto de todos os componentes. Após encaixar as rodas, certifique-se de que tudo esteja firme, estável e no lugar correto, evitando folgas ou desalinhamentos que possam prejudicar a performance. Finalize ajustando os freios com precisão para garantir a segurança e o bom funcionamento da bike durante o uso.
  </p>
</section>

<section>
  <h2>Instalação e Regulagem da Corrente</h2>
  <p>
    A instalação correta da corrente é fundamental para garantir o bom funcionamento e a segurança da máquina. Inicialmente, posicione a corrente cuidadosamente ao redor do guia, certificando-se de que os dentes estejam alinhados com as ranhuras do carrilhão. Após encaixá-la, verifique a tensão ajustando a corrente para que fique firme, mas com uma leve folga que permita seu movimento sem riscos de travamento. Uma regulagem inadequada pode causar desgaste prematuro da corrente e do equipamento, além de aumentar o risco de acidentes. Para medir a tensão ideal, pressione a corrente no ponto médio do guia: ela deve permitir um leve deslocamento, aproximadamente entre 3 e 5 milímetros. Por fim, antes de utilizar a ferramenta, reavalie a regulagem após os primeiros minutos de uso, pois a corrente pode se ajustar naturalmente durante o funcionamento. A manutenção periódica dessa regulagem é essencial para prolongar a vida útil da corrente e garantir um corte eficiente.
  </p>

  <h3>Passos para colocar e ajustar a corrente</h3>
  <p>
    Posicione a corrente começando pelo câmbio traseiro, garantindo que ela esteja bem alinhada. Em seguida, passe a corrente pelas rodas dentadas com cuidado, direcionando-a entre os roletes do câmbio formando um trajeto em formato de "S". Meça o comprimento da corrente para verificar se está adequado ao seu sistema; caso haja excesso de elos, corte-os para evitar folgas ou aperto excessivo. Para remover os elos, utilize um martelo, um prego do tamanho adequado e uma arruela para auxiliar na pressão do pino. Posicione o prego sobre o pino da corrente e bata com o martelo até que o pino seja retirado com cuidado. Após ajustar o tamanho e posicionar a corrente, utilize um alicate para pressionar o pino de volta, garantindo que ele fique firme; o encaixe correto será identificado ao ouvir dois cliques. Finalize verificando o esticamento da corrente, certificando-se de que não esteja folgada nem muito rígida, assegurando um funcionamento suave durante o uso.
  </p>
</section>

<section>
  <h2>Regulagem dos Componentes Principais</h2>
  <p>
    A regulagem correta dos componentes principais é essencial para garantir o desempenho ideal de qualquer sistema mecânico ou eletrônico. Cada componente deve ser ajustado conforme suas especificações técnicas, respeitando as margens de tolerância recomendadas pelo fabricante. O ajuste inadequado pode resultar em falhas, desgaste precoce e perda de eficiência operacional. Para realizar a regulagem, é necessário utilizar ferramentas apropriadas e seguir procedimentos padronizados, o que assegura precisão e segurança durante o processo. Além disso, a calibragem adequada dos principais elementos contribui para a otimização do consumo de energia e melhoria na resposta do sistema. Dessa forma, a manutenção preventiva baseada em regulagens periódicas evita paradas inesperadas e reduz custos de reparo, mantendo a integridade dos equipamentos.
  </p>

  <h3>Aperto do pedal e suporte do pé de vela</h3>
  <p>
    Verifique regularmente as porcas e parafusos dos pedais para garantir que estejam firmes e seguros. É importante apertar também a parte inferior do suporte do pedal, utilizando a chave Allen adequada, já que esses componentes podem vir soltos de fábrica. Durante o aperto, tome cuidado para não espanar as roscas ou danificar as peças, aplicando a força correta e evitando excessos. Manter o pedal e seu suporte bem ajustados contribui para a segurança e o desempenho do equipamento, evitando folgas que possam comprometer o uso contínuo. Essa manutenção preventiva assegura um funcionamento mais estável e confortável para o usuário.
  </p>

  <h3>2. Regulagem das manetes de freio e trocadores de marcha</h3>
  <ul>
    <li>Utilize uma chave Allen 4 para soltar levemente os parafusos das manetes de freio, permitindo o ajuste sem causar danos.</li>
    <li>Posicione as manetes de modo que fiquem confortáveis para as mãos, respeitando a ergonomia e garantindo funcionalidade ideal durante o uso.</li>
    <li>Aperte os parafusos em modo cruzado, alternando entre eles para evitar tensões desiguais e possíveis danos às peças.</li>
    <li>Para a regulagem do passador de marcha, utilize uma chave Allen 5 para afrouxar e posicionar corretamente o cabo, garantindo que ele tenha folga suficiente para um funcionamento suave e preciso.</li>
    <li>Ao ajustar o trocador, certifique-se de que o cabo esteja tensionado de maneira adequada, para que as mudanças de marcha sejam fluidas e sem travamentos.</li>
    <li>Finalize verificando o funcionamento geral após a regulagem e faça pequenos ajustes se necessário para maximizar o desempenho e conforto.</li>
  </ul>

  <h3>3. Ajuste do freio hidráulico</h3>
  <p>
    Para garantir a eficiência dos freios hidráulicos, comece acionando o freio com firmeza, o que permite que o sistema se estabilize antes do ajuste. Em seguida, aperte os parafusos que mantêm o conjunto fixo, assegurando que as peças estejam bem presas e alinhadas. Segure o freio com uma mão para manter a pressão constante, enquanto com a outra você aperta o parafuso de ajuste. Esse movimento deve ser feito com cuidado para não exagerar no aperto e comprometer o funcionamento do sistema. Após o ajuste inicial, verifique o funcionamento dos freios dianteiro e traseiro, observando o espaçamento entre as pastilhas e o disco. Faça os ajustes necessários até que o espaçamento esteja ideal, garantindo a segurança e a resposta eficiente durante a frenagem. Esse cuidado é fundamental para manter o desempenho e a durabilidade dos freios hidráulicos.
  </p>

  <h3>4. Regulagem do câmbio traseiro e passagem do cabo de aço</h3>
  <p>
    Posicione o câmbio traseiro a aproximadamente 2 mm da coroa, garantindo espaço suficiente para o movimento sem causar atrito. Em seguida, aperte o suporte utilizando uma chave 9, certificando-se de que esteja firme e alinhado. Ajuste os parafusos de regulagem de marcha com uma chave de fenda Phillips ou comum, para que o câmbio mova-se com precisão entre as engrenagens. Pedale testando a passagem das marchas e faça os ajustes finos necessários até que todas as marchas engatem sem hesitação ou ruídos.
  </p>
  <p>
    Para a instalação do cabo de aço, preste atenção para que a laçada do cabo seja feita do lado correto, evitando qualquer dano à estrutura ou mau funcionamento da transmissão. Aperte a porca de fixação para esticar o cabo adequadamente, o que é fundamental para garantir mudanças suaves e rápidas. Realize testes finais em todas as velocidades, verificando o funcionamento consistente do câmbio traseiro e corrigindo eventuais falhas para assegurar uma regulagem precisa e confiável.
  </p>
</section>

<section>
  <h2>Ajuste Final do Banco e Suporte</h2>
  <p>
    Posicione cuidadosamente o suporte do banco no quadro da bicicleta, garantindo que ele esteja alinhado corretamente para evitar desalinhamentos durante o uso. Utilize as chaves Allen 5 e Allen 6 para apertar os parafusos de fixação, aplicando uma pressão firme e estável, mas sem exageros que possam comprometer a integridade do suporte ou do quadro. Em seguida, ajuste a altura do banco conforme a preferência e conforto do ciclista, levando em consideração a amplitude do movimento das pernas e a postura ideal para pedalar. Esse ajuste é fundamental para melhorar a eficiência da pedalada e evitar desconfortos ou lesões durante o uso prolongado. Por fim, confira se todos os pontos de fixação estão devidamente apertados, garantindo a segurança e estabilidade do banco antes de seguir para a próxima etapa do processo.
  </p>
</section>

<section>
  <h2>Conclusão</h2>
  <p>
    A montagem da bicicleta aro 29, incluindo a instalação e regulagem da corrente, câmbio, freios, pedais e guidão, requer organização e atenção aos detalhes técnicos para garantir um resultado eficiente e seguro. Seguindo este passo a passo de forma cuidadosa, você assegura que todos os componentes estejam ajustados corretamente, contribuindo para um desempenho ideal e maior durabilidade da bicicleta. Além disso, a manutenção adequada durante a montagem evita problemas futuros e garante uma experiência mais agradável ao pedalar.
  </p>
  <p>
    Se desejar, compartilhe este guia para auxiliar outros apaixonados por bicicleta a realizarem suas próprias montagens com confiança e segurança.
  </p>
  <p>
    <strong>Dica final:</strong> Sempre leve sua bicicleta para um mecânico especializado caso não tenha experiência suficiente, principalmente para a regulagem fina das marchas e freios hidráulicos, garantindo assim sua segurança e o funcionamento perfeito do equipamento.
  </p>
</section>
</div>"""

content_teste2 = """<p>
  A bicicleta GTS M1 é uma excelente opção para quem busca qualidade e praticidade na sua primeira bike. Quando comprada pelo site oficial, ela chega diretamente até você, geralmente desmontada para facilitar o transporte. Com este guia, você aprenderá a realizar a montagem completa, utilizando as ferramentas necessárias e seguindo um procedimento simples e eficiente. Isso inclui fixar o guidão, ajustar o banco na altura correta, instalar as rodas e verificar o alinhamento dos freios e câmbio. Dessa forma, você garante que sua bicicleta esteja pronta para oferecer o melhor desempenho e segurança, pronta para as primeiras pedaladas com conforto e estabilidade.
</p>

<section>
  <h2>Ferramentas Necessárias para a Montagem</h2>
  <p>
    Para montar corretamente a bicicleta GTS M1, é fundamental ter à mão as ferramentas certas, garantindo um processo eficiente e seguro. Você precisará de um estilete ou faca afiada para abrir cuidadosamente as embalagens sem danificar os componentes. Além disso, uma chave 15 é essencial para apertar porcas e parafusos específicos do quadro e rodas. As chaves Allen nas medidas 6, 5 e 4 mm são indispensáveis para ajustar peças como o guidão, o selim e os freios, sendo necessário que elas tenham boa profundidade para alcançar parafusos mais profundos sem comprometer a fluidez do movimento durante a montagem. Ter essas ferramentas auxiliares facilita o trabalho e ajuda a evitar danos, garantindo que sua bicicleta fique pronta para uso de forma rápida e com segurança.
  </p>
</section>

<section>
  <h2>Componentes Incluídos na Caixa</h2>
  <p>
    A embalagem da bicicleta contém todos os itens essenciais para montagem e uso imediato. Entre os componentes incluídos estão o manual de instruções, que orienta passo a passo a montagem e manutenção do produto, e o selim, fundamental para o conforto durante as pedaladas. Também estão presentes os pedais, garantindo que a bicicleta esteja pronta para uso assim que montada, e o canote do selim, que permite ajustar a altura do assento conforme a necessidade do ciclista. Além disso, a embalagem traz a blocagem (quick release) para a roda dianteira, facilitando a fixação e remoção rápida da roda para transporte ou manutenção. Esses componentes asseguram que o usuário tenha tudo o que precisa para montar a bicicleta com facilidade, segurança e praticidade.
  </p>
</section>

<section>
  <h2>Passo a Passo para Montagem da Bicicleta GTS M1</h2>
  <p>
    Comece fixando o guidão ao garfo, assegurando que os parafusos estejam bem apertados para evitar folgas durante o uso. Em seguida, posicione a roda dianteira no garfo e aperte as porcas ou sistema de engate rápido, garantindo que ela esteja alinhada corretamente para uma dirigibilidade precisa. Depois, instale o câmbio dianteiro e traseiro, ajustando os cabos para que as marchas troquem suavemente. Verifique o correto posicionamento do selim e fixe-o na altura desejada, certificando-se de que está firme. Por fim, ajuste os freios para máximo desempenho, testando seu funcionamento para garantir segurança em todas as situações. Com essas etapas concluídas, sua bicicleta estará pronta para uso imediato.
  </p>

  <h3>1. Desembalando a Bicicleta</h3>
  <p>
    Utilize um estilete para cortar cuidadosamente as fitas plásticas que prendem a embalagem. Tome cuidado para não danificar as peças internas enquanto realiza o corte. Em seguida, abra a caixa para retirar a bicicleta e seus components destinados à montagem, manuseando-os com atenção para evitar arranhões ou amassados. Verifique se todas as peças essenciais estão presentes e em boas condições antes de prosseguir para a montagem. Esse cuidado inicial garante que o processo seguinte ocorra de forma segura e sem contratempos.
  </p>

  <h3>2. Montagem do Selim</h3>
  <ul>
    <li>Utilize a chave Allen 6 para prender o carrinho do selim na parte inferior do banco, garantindo que ele esteja alinhado corretamente e posicionado na altura desejada.</li>
    <li>Aperte firmemente os parafusos para fixar o selim com segurança, evitando folgas que possam comprometer o conforto e a estabilidade durante o uso.</li>
    <li>Certifique-se de que todos os parafusos estejam bem ajustados, mas sem exagerar na força para não danificar as roscas ou o próprio selim.</li>
    <li>Após a fixação, faça um teste rápido para verificar se o selim está firme e na posição adequada antes de prosseguir para as próximas etapas da montagem.</li>
  </ul>

  <h3>3. Montagem do Guidão</h3>
  <ul>
    <li>Solte os quatro parafusos do avanço do guidão utilizando a chave Allen 4, garantindo que todos sejam afrouxados de forma uniforme para facilitar o alinhamento.</li>
    <li>Encaixe o guidão no avanço e posicione-o na altura e ângulo desejados, ajustando conforme a preferência para maior conforto e controle durante o uso.</li>
    <li>Alinhe cuidadosamente o guidão, certificando-se de que esteja centralizado e nivelado em relação à roda dianteira, para evitar desconfortos ou riscos de segurança.</li>
    <li>Aperte novamente, com firmeza, os quatro parafusos utilizando a chave Allen 4, garantindo que o guidão fique bem fixo e estável durante todo o percurso.</li>
    <li>Verifique se todos os parafusos estão devidamente apertados e que o guidão não apresenta movimentos ou folgas que possam prejudicar a sua pilotagem.</li>
  </ul>

  <h3>4. Montagem da Roda Dianteira</h3>
  <ul>
    <li>Remova cuidadosamente a trava de segurança do freio hidráulico para evitar danos ao sistema durante a montagem.</li>
    <li>Posicione a roda dianteira no garfo, alinhando os eixos de forma precisa para garantir um encaixe correto.</li>
    <li>Utilize a blocagem para travar e fixar a roda no lugar, assegurando que ela esteja bem presa e alinhada, o que é fundamental para o funcionamento seguro e eficiente da bicicleta. Certifique-se de que a blocagem esteja bem apertada para evitar qualquer folga ou movimento indesejado durante o uso.</li>
  </ul>

  <h3>5. Montagem dos Pedais</h3>
  <p>
    Os pedais possuem identificação clara para garantir a instalação correta e segura na bicicleta:
  </p>
  <ul>
    <li>Pedal com rosca "R": deve ser instalado no lado direito da bicicleta, que é o lado do movimento para frente.</li>
    <li>Pedal com rosca "L": deve ser instalado no lado esquerdo, com rosca invertida para evitar que afrouxem durante o uso.</li>
  </ul>
  <p>
    Antes de rosquear, verifique se os encaixes estão limpos e lubrificados para facilitar a instalação e evitar desgastes prematuros. Rosqueie cada pedal na posição correta com as mãos inicialmente para evitar cruzar a rosca e depois aperte firmemente com uma chave apropriada. Isso garante que os pedais fiquem fixos, evitando movimentos indesejados que podem comprometer a segurança e o desempenho durante a pedalada.
  </p>
</section>

<section>
  <h2>Finalização e Recomendações</h2>
  <ul>
    <li>Verifique e aperte todos os parafusos principais da bicicleta, incluindo os do quadro, guidão, selim e pedais, garantindo que estejam firmes, mas sem excesso de aperto que possa danificar as peças.</li>
    <li>Alinhe o avanço do guidão e confirme que tudo está corretamente fixado e ajustado, para evitar desconforto ou riscos durante a pedalada.</li>
    <li>Inspecione também o aperto dos freios e das rodas, garantindo a segurança total antes de utilizar a bicicleta.</li>
  </ul>
  <p>
    É fundamental ressaltar que, após a montagem inicial em casa, é altamente recomendável levar a bicicleta a uma oficina especializada para uma regulagem completa e profissional. Essa manutenção garante o funcionamento perfeito da bike, corrigindo possíveis falhas que passam despercebidas, além de aumentar significativamente a durabilidade dos componentes. Com isso, você evita desgastes prematuros e assegura uma experiência mais confortável e segura ao pedalar.
  </p>
</section>

<section>
  <h2>Onde Comprar a Bicicleta GTS M1</h2>
  <p>
    Se você gostou desta bicicleta, a melhor opção é visitar o site oficial <a href="https://lojagtsm1.com.br" target="_blank" rel="noopener noreferrer">lojagtsm1.com.br</a>. No site, você encontra as promoções exclusivas, condições especiais de pagamento e toda a garantia de autenticidade do produto. Comprar diretamente na loja oficial também oferece vantagens como suporte técnico especializado, atendimento personalizado e a possibilidade de acompanhar o status do seu pedido em tempo real. Além disso, o site frequentemente disponibiliza ofertas por tempo limitado que garantem um excelente custo-benefício na aquisição do seu novo modelo GTS M1. Aproveite a comodidade de comprar online, com entrega rápida e segura, para começar a desfrutar da sua bicicleta o quanto antes.
  </p>
  <p>
    Com este guia, a montagem da bicicleta GTS M1 torna-se rápida, fácil e segura, permitindo que você aproveite ao máximo seu novo equipamento e garantir que ela tenha profundidade mantendo a fluidez do texto completo.
  </p>
</section>

</div>"""

content_teste3 = """<p>
  Este guia completo apresenta o passo a passo para montar uma bicicleta aro 29 adquirida nova, sem necessidade de levar ao mecânico. O processo é rápido, prático e detalhado, abordando desde a montagem básica até os ajustes essenciais, como regulagem de freios e marchas. Primeiramente, é importante conferir todas as peças e componentes caixas antes de iniciar a montagem, garantindo que nada esteja faltando ou danificado. Em seguida, comece fixando o guidão no avanço, certificando-se de que está alinhado corretamente com a roda dianteira. Depois, instale a roda dianteira no garfo, prendendo firmemente o eixo ou quick release. Posteriormente, encaixe o selim no canote, ajustando a altura conforme sua altura e conforto. Após essas etapas iniciais, ajuste os freios para que funcionem de maneira eficiente, fixando as pastilhas corretamente e regulando a tensão do cabo. Por fim, realize a regulagem das marchas, garantindo mudanças suaves e precisas para diferentes terrenos. Com atenção e calma, a montagem pode ser concluída em poucos minutos, deixando sua bike pronta para rodar.
</p>

<section>
  <h2>Recebendo e preparando a bicicleta para montagem</h2>
  <p>
    Ao receber a bike, ela chegará devidamente lacrada, com várias peças desmontadas e embaladas cuidadosamente em plástico e papelão para garantir a proteção durante o transporte. Antes de começar a montagem, é essencial conferir se todas as peças estão presentes e em perfeito estado, evitando surpresas desagradáveis durante o processo. Além disso, recomenda-se abrir as embalagens com cuidado para não danificar componentes sensíveis, como freios e sistema de mudança de marcha. Prepare um espaço limpo e organizado para facilitar a montagem, dispondo as ferramentas necessárias ao alcance das mãos. Essa etapa inicial é fundamental para garantir que todo o procedimento seguinte ocorra de forma tranquila e segura, preservando a integridade da bicicleta e facilitando o uso correto após a montagem.
  </p>

  <h3>Cuidados iniciais</h3>
  <p>
    Retire completamente todos os plásticos e embalagens protetoras, pois eles não oferecem proteção efetiva para as peças da bicicleta durante a montagem. Em seguida, separe cuidadosamente todas as partes que serão montadas, como pneus, assento, guidão, freios a disco, parafusos e pedais. Organizar esses itens previamente facilita o processo e evita perder componentes importantes. Tenha à mão as ferramentas básicas necessárias para a montagem, garantindo praticidade e eficiência. Entre elas, um jogo de chaves Allen, principalmente nos tamanhos 4 e 5 mm, é fundamental para apertar parafusos específicos. Também é importante contar com uma chave de boca 15 mm, ideal para a fixação do pedal. Utilize graxa lubrificante nas peças metálicas para evitar desgaste e garantir maior durabilidade. Por fim, mantenha uma fita métrica ou régua para conferir medidas precisas durante o ajuste, assegurando que tudo fique alinhado corretamente antes do uso.
  </p>
</section>

<section>
  <h2>Montagem inicial da bicicleta</h2>
  <p>
    A montagem inicial da bicicleta é um passo fundamental para garantir segurança e bom desempenho durante o uso. Comece fixando o guidão e ajustando sua altura conforme a preferência do ciclista, assegurando que esteja firme e alinhado com a roda dianteira. Em seguida, instale os pedais, conferindo se estão parafusados na direção correta para evitar danos às roscas. Verifique também a regulagem do selim, ajustando sua altura e inclinação para proporcionar conforto e eficiência na pedalada. Por fim, examine os freios e câmbios, certificando-se de que estão bem ajustados e funcionando corretamente. Um conjunto montado com atenção garante não apenas uma melhor experiência, mas também reduz riscos de acidentes e desgaste precoce dos componentes. Assim, a montagem correta prepara o terreno para um uso seguro e prazeroso da bicicleta.
  </p>

  <h3>1. Posicionar a bike para montagem</h3>
  <p>
    Deixe a bike em pé, apoiada de forma estável para facilitar a instalação das peças. É importante encontrar uma superfície plana e firme para garantir que a bicicleta não tombe durante o processo. Se possível, utilize um suporte ou cavalete específico para bike, pois isso facilita o acesso a todas as partes e permite trabalhar com mais precisão. Manter a bike corretamente posicionada também ajuda a evitar danos e acelera a montagem, tornando o procedimento mais seguro e eficiente. Assim, você assegura que cada componente seja instalado corretamente, preparando o terreno para as etapas seguintes da montagem.
  </p>

  <h3>2. Instalar o guidão</h3>
  <ul>
    <li>Solte os quatro parafusos da mesa do guidão usando uma chave Allen 4 mm, garantindo que eles fiquem completamente livres para a retirada da peça frontal.</li>
    <li>Retire cuidadosamente a peça frontal da mesa para encaixar o guidão, evitando forçar ou danificar as partes envolvidas.</li>
    <li>Certifique-se de posicionar os cabos para o lado correto, de modo que fiquem organizados e sem risco de enrosco ou desgaste prematuro.</li>
    <li>Posicione o guidão na posição central, utilizando uma fita métrica para medir e assegurar que as distâncias dos dois lados estejam exatamente iguais, o que garante equilíbrio e controle durante a pilotagem.</li>
    <li>Ajuste a altura do guidão para uma posição confortável, evitando que fique muito alto, o que pode comprometer a estabilidade, ou muito baixo, o que pode causar desconforto nas mãos e nas costas.</li>
    <li>Aperte os parafusos de forma uniforme e simultânea, utilizando a chave Allen, para evitar deformações ou danos à mesa do guidão, garantindo também maior segurança na fixação.</li>
    <li>Alinhe o guidão ao centro da suspensão, ajustando o parafuso da espiga (jogo central) para que o movimento da direção fique preciso e sem folgas.</li>
    <li>Finalmente, trave os dois parafusos laterais da mesa da direção, tomando cuidado para não apertar excessivamente, o que poderia causar quebra em quedas, mas mantendo firmeza suficiente para garantir que o guidão esteja seguro e estável.</li>
  </ul>

  <h3>Dicas importantes</h3>
  <p>
    Use uma pequena quantidade de graxa em peças que sofrem atrito para garantir o bom funcionamento e prolongar a vida útil dos componentes. Entre os pontos mais comuns estão: o pedal e o eixo do pedal, que precisam de lubrificação para evitar o desgaste pelo movimento constante; o pé de vela, cuja graxa minimiza o atrito e previne o travamento; e o eixo das rodas, que, devidamente lubrificado, facilita o giro suave e evita ruídos.
  </p>
  <p>
    É fundamental aplicar a graxa apenas onde o metal faz contato, evitando áreas onde ela possa acumular sujeira ou atrair poeira. Um cuidado especial deve ser tomado com a mesa do guidão: não deve-se aplicar graxa nessa região para evitar problemas como o deslizamento excessivo ou a corrosão em outras partes próximas. A lubrificação correta contribui para o funcionamento eficiente das peças, reduzindo o esforço durante o uso e prevenindo danos causados pelo atrito e pela oxidação.
  </p>
</section>

<section>
  <h2>Instalação do selim (banco)</h2>
  <ol>
    <li>Solte parcialmente o parafuso da abraçadeira do selim, tomando cuidado para não soltá-lo completamente, para facilitar o encaixe do canote.</li>
    <li>Encaixe o canote do selim no quadro da bicicleta, certificando-se de passar os cabos por dentro do quadro, caso sua bicicleta tenha essa configuração, para evitar complicações posteriores.</li>
    <li>Ajuste a inclinação do selim deixando-o alinhado e o mais reto possível, garantindo maior conforto e estabilidade durante a pilotagem.</li>
    <li>Segure firmemente o selim para evitar qualquer movimentação e, em seguida, aperte o parafuso da abraçadeira com força adequada, garantindo que o banco fique fixo e seguro.</li>
    <li>Para evitar que o canote trave ou enferruje com o tempo, aplique uma pequena quantidade de graxa na abraçadeira antes de apertá-la. Isso facilita futuras manutenções e prolonga a vida útil das peças.</li>
    <li>Preste atenção para não ultrapassar a marcação de segurança no canote, mantendo-o dentro do limite indicado e garantindo que ele não ultrapasse a solda superior do tubo do quadro, evitando danos estruturais à bicicleta.</li>
  </ol>
</section>

<section>
  <h2>Instalação da roda dianteira com freio a disco</h2>
  <ol>
    <li>Retire cuidadosamente o papelão ou protetor que envolve o disco de freio, garantindo que o disco fique livre para a instalação.</li>
    <li>Identifique o lado correto do disco, que normalmente vem marcado para facilitar a orientação, e posicione-o corretamente na roda.</li>
    <li>Parafuse os seis parafusos do disco utilizando uma chave Allen adequada, apertando-os de forma uniforme para evitar deformações.</li>
    <li>Coloque a roda no garfo dianteiro da bicicleta, alinhando o eixo com os encaixes no garfo.</li>
    <li>Utilize a blocagem (alavanca de trava rápida) para fixar firmemente a roda ao garfo, assegurando que a roda esteja correta e segura.</li>
    <li>Aplique uma pequena quantidade de graxa na blocagem para prevenir corrosão e facilitar a abertura em manutenções futuras.</li>
    <li>Evite sobre-apertar a blocagem para garantir a segurança da roda sem causar danos ao mecanismo ou ao garfo.</li>
  </ol>
</section>

<section>
  <h2>Instalação e regulagem dos freios mecânicos a disco</h2>
  <p>
    Para a instalação dos freios mecânicos a disco, comece fixando o suporte do freio ao quadro ou garfo da bicicleta, garantindo que esteja alinhado corretamente com o disco. Em seguida, posicione a pinça de freio de modo que as pastilhas fiquem paralelas ao rotor, evitando contato constante que cause desgaste prematuro. A regulagem da tensão do cabo deve ser feita com cuidado, ajustando a alavanca até que o freio responda de forma eficiente, sem folgas excessivas nem travamentos. Teste a rotação da roda para assegurar que o rotor não toque nas pastilhas quando o freio estiver solto. Caso necessário, ajuste as limitações da pinça para centralizá-la perfeitamente em relação ao disco. Esse processo é fundamental para o desempenho ideal dos freios, proporcionando segurança e controle na frenagem.
  </p>

  <h3>Passos para instalação do cabo de freio</h3>
  <ul>
    <li>Identifique os cabos de freio com comprimento adequado para cada posição, dianteiro e traseiro, garantindo que não fiquem nem muito curtos nem excessivamente longos para evitar falhas no funcionamento.</li>
    <li>Passe o cabo de aço cuidadosamente pelo conduíte (mangueira) correspondente ao freio dianteiro ou traseiro, assegurando que não haja dobras que impeçam o movimento suave.</li>
    <li>Aplique uma fina camada de graxa no cabo para facilitar seu deslizamento dentro do conduíte, prevenindo desgaste prematuro e funcionando como lubrificante.</li>
    <li>Prenda o conduíte na suspensão ou no quadro da bicicleta utilizando braçadeiras próprias, fixando-o firmemente para evitar movimentos indesejados durante o uso.</li>
    <li>Na pinça de freio mecânica, insira o cabo de aço e fixe-o firmemente no parafuso de aperto, garantindo que esteja bem preso para evitar folgas.</li>
    <li>Ajuste o tensionamento do cabo utilizando o parafuso de suporte, deixando o cabo ligeiramente esticado para garantir uma resposta rápida e precisa dos freios.</li>
    <li>Caso a manete do freio fique tocando o disco e não volte à posição inicial, lave o disco com cuidado para remover eventuais resíduos de graxa ou óleo que possam comprometer a eficiência da frenagem.</li>
    <li>Utilize o parafuso de ajuste na pinça para aproximar ou afastar as pastilhas do disco, regulando a distância ideal para garantir frenagem eficiente sem causar atrito excessivo que possa desgastar as peças.</li>
  </ul>
  <p>
    Esses passos fundamentais asseguram não apenas o funcionamento adequado do sistema de freios, mas também contribuem para a segurança e o conforto durante o uso da bicicleta.
  </p>
</section>

<section>
  <h2>Montagem e regulagem das marchas</h2>
  <p>
    A montagem adequada das marchas é fundamental para garantir o desempenho eficiente de qualquer transmissão mecânica. Durante esse processo, é importante verificar cada engrenagem com atenção para assegurar que elas estejam posicionadas corretamente e alinhadas de forma precisa, evitando desgastes prematuros e problemas futuros. A regulagem das marchas deve ser feita com cuidado, ajustando folgas e tensões para que a troca ocorra de forma suave e sem ruídos. Além disso, o sincronismo entre as engrenagens precisa ser revisado para garantir que o sistema funcione com máxima eficiência e durabilidade. Um ajuste correto contribui para a segurança, o conforto na condução e prolonga a vida útil dos componentes envolvidos.
  </p>

  <h3>Montagem dos cabos e conduítes</h3>
  <p>
    Os cabos de marcha possuem comprimentos distintos para o câmbio dianteiro e traseiro, o que é fundamental para garantir o funcionamento correto do sistema. O cabo do câmbio dianteiro, normalmente, é passado do lado esquerdo para o direito, seguindo pelo guidão para facilitar o manuseio e evitar interferências. Durante a montagem, é importante passar o cabo junto com o conduíte, aplicando uma fina camada de graxa para assegurar a lubrificação adequada e facilitar o movimento suave do cabo dentro do conduíte. Além disso, utilize as capas plásticas de acabamento para proteger a passagem do cabo, evitando o contato direto com elementos que possam causar ferrugem ou desgaste prematuro. Esses cuidados são essenciais para manter a durabilidade do sistema de câmbio e garantir uma troca de marchas eficiente e precisa.
  </p>

  <h3>Regulagem das marchas</h3>
  <ul>
    <li>Deixe o passador de marcha na posição inicial, que corresponde à última marcha. Isso facilita o ajuste correto do cabo e evita tensionamento indevido durante a regulagem.</li>
    <li>Prenda o cabo no câmbio utilizando uma chave adequada, normalmente uma chave de 9 mm, garantindo que ele fique firmemente fixado no local correto sem folgas.</li>
    <li>Ajuste a tensão do cabo com os parafusos de regulagem localizados no passador de marcha. Faça esse ajuste cuidadosamente, girando os parafusos até que as marchas passem com suavidade e precisão, sem pulos ou engate difícil.</li>
    <li>Caso o cabo esteja frouxo, reaplique os ajustes nos parafusos até que o sistema de troca de marchas funcione corretamente, mantendo a tensão ideal para evitar desgastes prematuros e garantir uma condução mais confortável.</li>
  </ul>
  <p>
    Essa rotina de regulagem deve ser feita sempre que perceber que as trocas de marcha não estão precisas ou quando o cabo for substituído, garantindo o desempenho ideal do sistema de câmbio.
  </p>
</section>

<section>
  <h2>Instalação dos pedais</h2>
  <ol>
    <li>Antes de instalar os pedais, aplique uma fina camada de graxa específica nas roscas para evitar que eles grudem com o tempo devido à oxidação ou sujeira. Essa ação também facilita a remoção futura dos pedais, preservando a integridade das roscas.</li>
    <li>É fundamental observar que os pedais possuem roscas diferenciadas para evitar apertos incorretos:
      <ul>
        <li>Lado direito: rosca no sentido horário (apertar girando para frente).</li>
        <li>Lado esquerdo: rosca no sentido anti-horário (apertar girando para trás).</li>
      </ul>
      Essa característica garante que os pedais não se soltem durante o uso.
    </li>
    <li>Utilize uma chave de 15 mm para apertar os pedais com firmeza, sem exageros que possam danificar as roscas ou os braços do pedal. Um aperto adequado assegura a segurança e o bom funcionamento dos pedais enquanto você pedala.</li>
  </ol>
  <p>
    Seguindo esses passos, a instalação será eficiente e duradoura, facilitando o desempenho e a manutenção da sua bicicleta.
  </p>
</section>

<section>
  <h2>Considerações finais e dicas importantes</h2>
  <p>
    A montagem de uma bicicleta aro 29 nova exige atenção especial à regulagem dos freios e das marchas, pois são as partes mais delicadas e que impactam diretamente no desempenho e na segurança do ciclista. O uso correto de graxa em pontos estratégicos, como pedal, eixo das rodas e canote do selim, é essencial para evitar corrosão e facilitar a manutenção futura, aumentando a durabilidade dos componentes. No exemplo apresentado, a bicicleta foi adquirida por cerca de R$ 800,00 em uma grande loja de varejo, o que demonstra a possibilidade de montar um modelo básico, porém reforçado, com ótimo custo-benefício. Além disso, ao montar sua própria bike, você aprende sobre o funcionamento dos componentes, economiza dinheiro e ganha autonomia para realizar pequenos reparos e ajustes sempre que necessário. Para dúvidas específicas sobre regulagem dos freios ou das marchas, é recomendável consultar vídeos e tutoriais especializados, garantindo um ajuste perfeito e seguro.
  </p>
  <p>
    Ao seguir este guia, você poderá montar sua bike aro 29 de forma segura e eficiente, pronta para seus passeios e aventuras sem depender do mecânico.
  </p>
</section>

</div>"""

replace_content("src/pages/blog/teste1.astro", content_teste1, "Como Montar uma Bicicleta Aro 29: Guia Completo Passo a Passo", "Este artigo detalha o processo completo para montar uma bicicleta aro 29, desde a organização das peças até a regulagem final dos componentes.")
replace_content("src/pages/blog/teste2.astro", content_teste2, "Montagem da Bicicleta GTS M1: Passo a Passo Completo", "Aprenda a realizar a montagem completa da bicicleta GTS M1, utilizando as ferramentas necessárias e seguindo um procedimento simples e eficiente.")
replace_content("src/pages/blog/teste3.astro", content_teste3, "Como montar uma bike aro 29 direto da fábrica", "Este guia completo apresenta o passo a passo para montar uma bicicleta aro 29 adquirida nova, sem necessidade de levar ao mecânico.")

print("Feito com sucesso!")
