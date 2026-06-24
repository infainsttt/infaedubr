from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto
)

from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

import os
TOKEN = os.getenv("TOKEN")

LINK_MATRICULA = "https://t.me/infaedufilialbr"


# -----------------------------
# FUNÇÃO DE EDIÇÃO DE TELA
# -----------------------------
async def editar_tela(query, imagem, texto, teclado):
    media = InputMediaPhoto(
        media=open(imagem, "rb"),
        caption=texto
    )

    await query.edit_message_media(
        media=media,
        reply_markup=teclado
    )


async def enviar_detalhamento(query, context, texto):

    try:
        msg_antiga = context.user_data.get("detalhamento")

        if msg_antiga:
            await context.bot.delete_message(
                chat_id=query.message.chat.id,
                message_id=msg_antiga
            )
    except:
        pass

    msg = await query.message.chat.send_message(texto)

    context.user_data["detalhamento"] = msg.message_id


async def apagar_detalhamento(query, context):

    try:
        msg_antiga = context.user_data.get("detalhamento")

        if msg_antiga:
            await context.bot.delete_message(
                chat_id=query.message.chat.id,
                message_id=msg_antiga
            )

            context.user_data["detalhamento"] = None
    except:
        pass
# -----------------------------
# START
# -----------------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    teclado = InlineKeyboardMarkup([
        [InlineKeyboardButton("1️⃣ Quero conhecer os cursos e garantir minha vaga", callback_data="MENU_CURSOS")],
        [InlineKeyboardButton("2️⃣ Já Sou Aluno e preciso de suporte", callback_data="ALUNO")],
        [InlineKeyboardButton("🔄 Desejo Retomar os Estudos", callback_data="RETOMAR")],
        [InlineKeyboardButton("0️⃣ Falar diretamente com Atendente", callback_data="DUVIDAS")]
    ])

    with open("imagens/inicio.jpg", "rb") as foto:
        await update.message.reply_photo(
            photo=foto,
            caption="🎓🧡 Bem-vindo(a) ao Instituto INFA!🧡🎓\n\nPara que possamos te atender da melhor forma, selecione uma das opções abaixo:",
            reply_markup=teclado
        )


# -----------------------------
# MENU INÍCIO
# -----------------------------
async def menu_inicio(query):

    teclado = InlineKeyboardMarkup([
        [InlineKeyboardButton("1️⃣ Quero conhecer os cursos e garantir minha vaga", callback_data="MENU_CURSOS")],
        [InlineKeyboardButton("2️⃣ Já Sou Aluno e preciso de suporte", callback_data="ALUNO")],
        [InlineKeyboardButton("🔄 Desejo Retomar os Estudos", callback_data="RETOMAR")],
        [InlineKeyboardButton("0️⃣ Falar diretamente com Atendente", callback_data="DUVIDAS")]
    ])

    await editar_tela(
        query,
        "imagens/inicio.jpg",
        "🎓🧡 Bem-vindo(a) ao Instituto INFA!🧡🎓\n\nPara que possamos te atender da melhor forma, selecione uma das opções abaixo:",
        teclado
    )


# -----------------------------
# MENU CURSOS
# -----------------------------
async def menu_cursos(query):

    teclado = InlineKeyboardMarkup([
        [InlineKeyboardButton("1️⃣ Gestão & Processos Administrativos", callback_data="CURSO_ADMIN")],
        [InlineKeyboardButton("2️⃣ Front Office Estratégico ", callback_data="CURSO_LOG")],
        [InlineKeyboardButton("3️⃣ Secretariado Administrativo ", callback_data="CURSO_REC")],
        [InlineKeyboardButton("4️⃣ Contact Center Profissional", callback_data="CURSO_ALM")],
        [InlineKeyboardButton("↩️ Voltar ao início", callback_data="INICIO")]
    ])

    await editar_tela(
        query,
        "imagens/inicio.jpg",
        "📚 Selecione o curso desejado:",
        teclado
    )


# -----------------------------
# CURSOS
# -----------------------------
async def curso_admin(query, context):

    await enviar_detalhamento(query,context,
"📋 CONTEÚDO PROGRAMÁTICO\n\n"
"📘 Gestão e Processos Administrativos\n\n"
"📱 100% Online | ⏱️ 08 horas | Este programa vai além das rotinas administrativas convencionais.\n\n"
"A área administrativa é um dos pilares fundamentais para o funcionamento eficiente de qualquer organização. Empresas modernas dependem de profissionais capazes de organizar processos, controlar atividades, apoiar a tomada de decisões e garantir a fluidez das operações internas.\n\n"
"A Gestão e os Processos Administrativos não se limitam à execução de tarefas — representam a base da organização empresarial, responsáveis por promover produtividade, controle operacional e suporte estratégico aos diversos setores da empresa.\n"
"Profissionais com domínio em organização administrativa, gestão de processos, controle documental, planejamento operacional e rotinas corporativas são altamente valorizados no mercado atual.\n\n"
"Pensando nisso, foi desenvolvida a Formação em Gestão e Processos Administrativos, um programa estruturado para elevar o nível técnico e operacional do aluno, preparando-o para atuar com eficiência, organização e alta performance em ambientes corporativos.\n\n"
"🎯 COMO O CURSO FUNCIONA:\n\n"
"Formação 100% prática, organizada em 5 módulos estratégicos, com foco na aplicação real das rotinas administrativas e dos processos organizacionais:\n\n"
"📋 Módulo 1 – Fundamentos da Gestão Administrativa\n\n"
"Estrutura organizacional e funcionamento das empresas\n"
"Papel do profissional administrativo nas organizações\n"
"Postura, ética e conduta no ambiente corporativo\n\n"
"🗂 Módulo 2 – Organização e Rotinas Administrativas\n\n"
"Controle de documentos e arquivos\n"
"Gestão de informações e fluxos administrativos\n"
"Padronização de processos e procedimentos internos\n\n"
"📊 Módulo 3 – Gestão de Processos e Apoio Operacional\n\n"
"Mapeamento e organização de processos administrativos\n"
"Controle de atividades, prazos e demandas internas\n"
"Otimização de rotinas e produtividade organizacional\n\n"
"💻 Módulo 4 – Ferramentas Administrativas e Controles\n\n"
"Utilização de sistemas e ferramentas corporativas\n"
"Elaboração de relatórios e registros administrativos\n"
"Acompanhamento de indicadores e controles operacionais\n\n"
"⚙️ Módulo 5 – Eficiência Operacional e Alta Performance\n\n"
"Planejamento e organização do trabalho\n"
"Resolução de problemas administrativos\n"
"Melhoria contínua e desempenho profissional\n\n"
"🔑 POSICIONAMENTO PROFISSIONAL:\n\n"
"💰 Investimento de acesso: R$ 139,00\n\n"
"O programa foi estruturado para oferecer uma formação acessível, mantendo um padrão técnico voltado às exigências reais do mercado administrativo e corporativo.\n"
"As turmas são organizadas de forma controlada para garantir melhor aproveitamento, qualidade de entrega e foco no desenvolvimento profissional do aluno.\n\n"
"💡 COMPETÊNCIAS DESENVOLVIDAS\n\n"
"🛡 Organização Administrativa Profissional\n"
"Gestão de documentos, informações e processos com padrão corporativo.\n\n"
"🔍 Gestão de Processos Administrativos\n"
"Capacidade de estruturar, acompanhar e otimizar rotinas organizacionais.\n\n"
"⚡ Planejamento e Controle Operacional\n"
"Desenvolvimento de práticas voltadas à eficiência e produtividade empresarial.\n\n"
"📊 Ferramentas e Sistemas Administrativos\n"
"Utilização de recursos tecnológicos para controle e suporte às operações.\n\n"
"📈 Alta Performance em Ambientes Corporativos\n"
"Atuação estruturada em setores administrativos e de apoio à gestão.\n\n"
"📈 PROPOSTA DE FORMAÇÃO\n\n"
"A proposta desta formação é desenvolver profissionais preparados para atuar na área administrativa moderna, com foco em organização, eficiência operacional e gestão de processos corporativos.\n\n"
"✅ ACESSO À FORMAÇÃO\n\n"
"Complete sua matrícula pelo Link :\n\n"
"https://compraonlinesegurada.org.ua/c/5d184c77f2\n\n"
"E nos envie o comprovante pela primeira opção do menu abaixo\n\n"
"Ou envie suas informações após clicar no primeiro botão abaixo:\n\n"
"Inscrição – Nome Completo: registro para liberação de acesso\n"
"Identificação – CPF: utilizado para emissão do certificado\n"
"Acesso Imediato – E-mail: envio das credenciais de acesso à plataforma\n"
)

    teclado = InlineKeyboardMarkup([
    [InlineKeyboardButton("✅ Matricule-se Agora", url="https://t.me/infaedufilialbr?text=Ol%C3%A1!%20Quero%20concluir%20a%20minha%20matr%C3%ADcula%20no%20curso%20Gest%C3%A3o%20e%20Processos%20Administrativos.")],
    [InlineKeyboardButton("❌ Cancelar", callback_data="INICIO")],
    [InlineKeyboardButton("↩️ Voltar", callback_data="MENU_CURSOS")]
])

    await query.message.chat.send_message(
        "Selecione uma das opções abaixo para prosseguir com o atendimento:\n"
        "                              \n"
        "🔽",
        reply_markup=teclado
)

async def curso_log(query, context):

    await enviar_detalhamento(query,context,
"⏳ ACESSO LIBERADO POR TEMPO LIMITADO\n"
"⚠️ ENCERRAMENTO IMINENTE DA CONDIÇÃO PROMOCIONAL\n"
"━━━━━━━━━━━━━━━━━━\n\n"
"🏢 FRONT OFFICE ESTRATÉGICO\n"
"Imagem Profissional, Comunicação Corporativa e Gestão da Experiência no Atendimento\n"
"━━━━━━━━━━━━━━━━━━\n"
"INSTITUTO INFA | Formação Profissional Avançada\n\n"
"De R$ 297,00 → R$ 139,00 (condição especial ativa)\n"
"📱 100% Online | ⏱️ 10 horas | 🎓 Certificado profissional\n\n"
"──────────────────\n"
"POSICIONAMENTO DO CURSO\n"
"──────────────────\n"
"Este programa vai além do atendimento convencional.\n"
"O Front Office Estratégico forma profissionais preparados para atuar com visão organizacional, postura corporativa e foco em eficiência operacional, contribuindo diretamente para a fluidez e qualidade dos processos internos de empresas, clínicas e ambientes administrativos.\n"
"Aqui você não aprende apenas a atender — você aprende a operar com padrão profissional elevado.\n"
"──────────────────\n"
"📚MÓDULOS DO CURSO\n"
"──────────────────\n"
"Módulo 01 — O Profissional de Front Office no Mercado Atual\n"
"Entenda o novo padrão exigido pelas empresas e como se posicionar de forma competitiva no mercado.\n\n"
"Módulo 02 — Imagem Profissional e Protocolo Corporativo\n"
"Aprenda postura, apresentação e comportamento alinhado ao ambiente corporativo de alto padrão.\n"
"Módulo 03 — Comunicação Corporativa Estratégica\n"
"Desenvolva uma comunicação clara, profissional e eficaz em todos os canais de atendimento.\n\n"
"Módulo 04 — Experiência do Cliente e Percepção de Valor\n"
"Aprenda a transformar o atendimento em uma experiência positiva e memorável.\n\n"
"Módulo 05 — Organização e Fluxo Operacional do Atendimento\n"
"Estruture rotinas e processos para garantir eficiência e evitar falhas no atendimento.\n\n"
"Módulo 06 — Gestão de Situações Críticas e Conflitos\n"
"Saiba lidar com pressão, reclamações e situações difíceis com postura profissional.\n\n"
"Módulo 07 — Alta Performance e Desenvolvimento de Carreira\n"
"Construa um posicionamento sólido para crescimento profissional e novas oportunidades.\n\n"
"──────────────────\n"
"O QUE VOCÊ VAI APRENDER NA PRÁTICA\n"
"──────────────────\n"
"🔹 Organização de processos para aumentar eficiência no atendimento\n"
"🔹 Comunicação estratégica com clientes e equipe\n"
"🔹 Padronização de rotinas para melhorar resultados operacionais\n"
"🔹 Controle de situações de pressão com postura profissional\n"
"🔹 Posicionamento como profissional de alto valor no ambiente corporativo\n\n"
"──────────────────\n"
"RESULTADO ESPERADO\n"
"──────────────────\n\n"
"✔️ Atuação com postura profissional e visão estratégica\n"
"✔️ Melhora significativa na organização e qualidade do atendimento\n"
"✔️ Destaque em processos seletivos e crescimento interno\n"
"✔️ Maior maturidade profissional e controle emocional\n"
"✔️ Capacidade de atuar em ambientes exigentes com excelência\n\n"
"──────────────────\n"
"BÔNUS ESTRATÉGICOS\n"
"──────────────────\n\n"
"📄 Currículo profissional atualizado para área administrativa e atendimento\n"
"📋 Checklist de padrão corporativo de atendimento\n"
"💬 Modelo profissional de comunicação para os canais oficiais do seu atendimento.\n"
"🎯 Plano de desenvolvimento profissional (PDI estruturado)\n\n"
"──────────────────\n"
"POR QUE GARANTIR AGORA?\n"
"──────────────────\n"
"🔒 Menor valor já aplicado neste treinamento\n"
"⚡️ Acesso vítalicio e imediato após confirmação da matrícula\n"
"🎁 Bônus disponíveis somente neste período\n"
"🔄 Garantia de 7 dias (risco zero)\n"
"🇧🇷 Certificação válida em todo o país.\n"
"🔖A emissão do certificado digital é opcional e realizada mediante taxas administrativas, destinadas à validação, registro de carga horária e autenticação do documento conforme critérios institucionais.\n"
"──────────────────\n"
"MATRÍCULA IMEDIATA\n"
"──────────────────\n\n"
"Complete sua matrícula pelo Link :\n\n"
"E nos envie o comprovante pela primeira opção do menu abaixo\n\n"

"Ou Envie seus dados para liberação:\n\n"
"👤 Nome completo\n"
"📧 E-mail\n"
"🪪 CPF\n\n"
"Após o envio, será liberado o QR Code Pix para pagamento imediato e iniciação da sua matrícula\n"
"━━━━━━━━━━━━━━━━━━\n"
"🚀 ACESSO POR R$ 139,00 — ÚLTIMAS VAGAS\n"
)

    teclado = InlineKeyboardMarkup([
    [InlineKeyboardButton("✅ Matricule-se Agora", url="https://t.me/infaedufilialbr?text=Ol%C3%A1!%20Quero%20concluir%20a%20minha%20matr%C3%ADcula%20no%20curso%20Front%20Office%20Estrat%C3%A9gico.")],
    [InlineKeyboardButton("❌ Cancelar", callback_data="INICIO")],
    [InlineKeyboardButton("↩️ Voltar", callback_data="MENU_CURSOS")]
])

    await query.message.chat.send_message(
        "Selecione uma das opções abaixo para prosseguir com o atendimento:\n"
        "                              \n"
        "🔽",
        reply_markup=teclado
)

async def curso_rec(query, context):

    await enviar_detalhamento(query,context,
"📘 Formação em Secretariado Administrativo\n"
"📱 100% Online | ⏱️ 08 horas | Este programa vai além do atendimento convencional.\n\n"
"A área administrativa é o núcleo operacional de qualquer organização moderna. É ela quem sustenta processos, organiza fluxos internos, garante a integridade das informações e mantém a comunicação corporativa funcionando de forma estruturada e eficiente.\n"
"Profissionais com domínio em rotinas administrativas, organização documental, atendimento profissional, sistemas internos e comunicação corporativa são cada vez mais valorizados em empresas de todos os portes — especialmente por sua capacidade de manter ordem, eficiência e continuidade operacional.\n"
"Pensando nisso, foi desenvolvida a Formação em Secretariado Administrativo, um programa estruturado para elevar o nível técnico e comportamental do aluno, preparando-o para atuar com organização, responsabilidade e alto desempenho em ambientes corporativos.\n\n"
"---\n"
"🎯 COMO O CURSO FUNCIONA:\n"
"Formação 100% prática, organizada em 5 módulos estratégicos, com foco na aplicação real das rotinas administrativas dentro de empresas e escritórios:\n\n"
"---\n"
"📋 Módulo 1 – Fundamentos do Secretariado Administrativo\n"
"Estrutura organizacional e funcionamento de empresas\n"
"Papel do profissional administrativo nas rotinas corporativas\n"
"Postura profissional, ética e conduta no ambiente de trabalho\n\n"
"---\n"
"💬 Módulo 2 – Comunicação e Atendimento Corporativo\n"
"Atendimento presencial, telefônico e digital\n"
"Comunicação clara, profissional e orientada a soluções\n"
"Relacionamento com clientes internos e externos\n\n"
"---\n"
"🗂 Módulo 3 – Gestão Administrativa e Organização de Processos\n"
"Controle e organização de documentos e arquivos\n"
"Gestão de agendas, demandas e fluxos internos\n"
"Padronização de rotinas administrativas\n\n"
"---\n"
"💻 Módulo 4 – Ferramentas Digitais e Processos Operacionais\n"
"Utilização de sistemas administrativos e ferramentas digitais\n"
"Planilhas de controle e organização de informações\n"
"Lançamento e acompanhamento de dados operacionais\n\n"
"---\n"
"⚙️ Módulo 5 – Rotinas Corporativas e Suporte Organizacional\n"
"Apoio a equipes e setores administrativos\n"
"Gestão de prioridades e demandas internas\n"
"Otimização de processos e melhoria de eficiência operacional\n\n"
"---\n"
"🔑 POSICIONAMENTO PROFISSIONAL:\n"
"💰 Investimento de acesso: R$ 139,00\n"
"O programa foi estruturado para oferecer uma formação acessível, mantendo um padrão técnico e organizacional voltado ao mercado de trabalho.\n"
"As turmas são organizadas de forma controlada para garantir melhor aproveitamento, qualidade de entrega e foco no desenvolvimento profissional do aluno.\n\n"
"---\n"
"💡 COMPETÊNCIAS DESENVOLVIDAS\n"
"🛡Organização Administrativa Profissional\n"
"Estruturação de documentos, registros e informações com padrão corporativo.\n"
"🔍 Gestão de Rotinas e Processos Internos\n"
"Capacidade de organizar fluxos, demandas e atividades administrativas com eficiência.\n"
"⚡ Comunicação Corporativa Aplicada\n"
"Desenvolvimento de postura, linguagem e conduta profissional no ambiente de trabalho.\n"
"📊 Ferramentas e Controle Operacional\n"
"Uso de recursos digitais para apoio à organização e tomada de decisão.\n"
"📈 Suporte Administrativo em Ambientes Corporativos\n"
"Atuação estruturada em rotinas de apoio a setores e equipes organizacionais.\n\n"
"---\n"
"📈 PROPOSTA DE FORMAÇÃO\n"
"A proposta desta formação é desenvolver profissionais com base sólida em rotinas administrativas, preparados para atuar com organização, responsabilidade e visão prática do ambiente corporativo.\n"
"---\n"
"✅ ACESSO À FORMAÇÃO\n"
"1. Inscrição – Nome Completo: registro para liberação de acesso\n"
"2. Identificação – CPF: utilizado para emissão do certificado\n"
"3. Acesso Imediato – E-mail: envio das credenciais de acesso à plataforma\n"
)
    teclado = InlineKeyboardMarkup([
    [InlineKeyboardButton("✅ Matricule-se Agora", url="https://t.me/infaedufilialbr?text=Ol%C3%A1!%20Quero%20concluir%20a%20minha%20matr%C3%ADcula%20no%20curso%20Secretariado%20Administrativo.")],
    [InlineKeyboardButton("❌ Cancelar", callback_data="INICIO")],
    [InlineKeyboardButton("↩️ Voltar", callback_data="MENU_CURSOS")]
])

    await query.message.chat.send_message(
        "Selecione uma das opções abaixo para prosseguir com o atendimento:\n"
        "                              \n"
        "🔽",
        reply_markup=teclado
)

async def curso_alm(query, context):

    await enviar_detalhamento(query,context,
"📘 Contact Center Profissional\n\n"
"📱 100% Online | ⏱️ 08 horas | Este programa vai além do atendimento convencional.\n\n"
"O setor de atendimento ao cliente evoluiu e se tornou uma das áreas mais estratégicas dentro das empresas modernas. Hoje, organizações dependem de profissionais capazes de atuar com comunicação eficiente, resolução de problemas, agilidade operacional e excelência no relacionamento com o cliente.\n\n"
"O Contact Center não é apenas um canal de atendimento — é o ponto central da experiência do cliente, responsável por garantir qualidade, organização das demandas e fortalecimento da imagem da empresa.\n\n"
"Profissionais com domínio em atendimento multicanal, comunicação profissional, sistemas de suporte, resolução de conflitos e rotinas operacionais são altamente valorizados no mercado atual.\n\n"
"Pensando nisso, foi desenvolvida a Formação em Contact Center Profissional, um programa estruturado para elevar o nível técnico e comportamental do aluno, preparando-o para atuar com excelência, postura profissional e alta performance em ambientes de atendimento.\n\n"
"🎯 COMO O CURSO FUNCIONA:\n\n"
"Formação 100% prática, organizada em 5 módulos estratégicos, com foco na aplicação real das rotinas de atendimento e suporte ao cliente:\n\n"
"📋 Módulo 1 – Fundamentos do Contact Center Profissional\n"
"Estrutura e funcionamento de operações de atendimento\n"
"Papel do profissional no relacionamento com o cliente\n"
"Postura, ética e conduta no ambiente de atendimento\n\n"
"💬 Módulo 2 – Comunicação e Atendimento ao Cliente\n"
"Atendimento presencial, telefônico e digital\n"
"Comunicação clara, objetiva e orientada à solução\n"
"Técnicas de abordagem e experiência do cliente\n\n"
"🗂 Módulo 3 – Gestão de Demandas e Processos de Atendimento\n"
"Organização de chamados e solicitações\n"
"Controle de fluxos de atendimento e prioridades\n"
"Padronização de respostas e procedimentos\n\n"
"💻 Módulo 4 – Sistemas e Ferramentas de Atendimento\n"
"Uso de sistemas de CRM e plataformas de atendimento\n"
"Registro de informações e histórico de clientes\n"
"Acompanhamento e controle de interações\n\n"
"⚙️ Módulo 5 – Resolução de Problemas e Alta Performance\n"
"Gestão de conflitos e situações críticas\n"
"Atendimento sob pressão com qualidade e eficiência\n"
"Melhoria contínua e desempenho profissional\n\n"
"🔑 POSICIONAMENTO PROFISSIONAL:\n\n"
"💰 Investimento de acesso: R$ 139,00\n\n"
"O programa foi estruturado para oferecer uma formação acessível, mantendo um padrão técnico voltado às exigências reais do mercado de atendimento e suporte ao cliente.\n\n"
"As turmas são organizadas de forma controlada para garantir melhor aproveitamento, qualidade de entrega e foco no desenvolvimento profissional do aluno.\n\n"
"💡 COMPETÊNCIAS DESENVOLVIDAS\n\n"
"🛡 Organização de Atendimento Profissional\n"
"Gestão de chamados, registros e fluxos de atendimento com padrão corporativo.\n\n"
"🔍 Gestão de Processos de Suporte ao Cliente\n"
"Capacidade de organizar demandas e resolver solicitações com eficiência.\n\n"
"⚡ Comunicação Profissional e Experiência do Cliente\n"
"Desenvolvimento de postura, linguagem e conduta voltada ao atendimento.\n\n"
"📊 Ferramentas e Sistemas de Atendimento (CRM)\n"
"Uso de plataformas digitais para registro e acompanhamento de clientes.\n\n"
"📈 Alta Performance em Atendimento ao Cliente\n"
"Atuação estruturada em ambientes dinâmicos e de alta demanda.\n\n"
"📈 PROPOSTA DE FORMAÇÃO\n\n"
"A proposta desta formação é desenvolver profissionais preparados para atuar no setor de atendimento moderno, com foco em eficiência operacional, comunicação profissional e excelência na experiência do cliente.\n\n"
"✅ ACESSO À FORMAÇÃO\n"
"Inscrição – Nome Completo: registro para liberação de acesso\n"
"Identificação – CPF: utilizado para emissão do certificado\n"
"Acesso Imediato – E-mail: envio das credenciais de acesso à plataforma\n"
)
    teclado = InlineKeyboardMarkup([
    [InlineKeyboardButton("✅ Matricule-se Agora", url="https://t.me/infaedufilialbr?text=Ol%C3%A1!%20Quero%20concluir%20a%20minha%20matr%C3%ADcula%20no%20curso%20Contact%20Center%20Profissional.")],
    [InlineKeyboardButton("❌ Cancelar", callback_data="INICIO")],
    [InlineKeyboardButton("↩️ Voltar", callback_data="MENU_CURSOS")]
])

    await query.message.chat.send_message(
        "Selecione uma das opções abaixo para prosseguir com o atendimento:\n"
        "                              \n"
        "🔽",
        reply_markup=teclado
)

# -----------------------------
# CALLBACKS
# -----------------------------
async def callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    if query.data == "INICIO":
        await apagar_detalhamento(query, context)
        await menu_inicio(query)

    elif query.data == "MENU_CURSOS":
        await apagar_detalhamento(query, context)
        await menu_cursos(query)

    elif query.data == "CURSO_ADMIN":
        await curso_admin(query, context)

    elif query.data == "CURSO_LOG":
        await curso_log(query, context)

    elif query.data == "CURSO_REC":
        await curso_rec(query, context)

    elif query.data == "CURSO_ALM":
        await curso_alm(query, context)

    elif query.data == "ALUNO":

        teclado = InlineKeyboardMarkup([
            [InlineKeyboardButton("🆘 Entre em contato com o suporte", url="https://t.me/infaedufilialbr?text=Ol%C3%A1!%20J%C3%A1%20sou%20aluno(a)%20e%20preciso%20de%20suporte.%20Minha%20matr%C3%ADcula%20%C3%A9:%20INSIRA%20SUA%20MATR%C3%8DCULA")],
            [InlineKeyboardButton("🏠 Voltar ao início", callback_data="INICIO")]
        ])

        await editar_tela(
            query,
            "imagens/inicio.jpg",
            "📚 Bem-vindo(a) Área do Aluno\n\nTenha sua o número da matrícula em mãos para obter suporte.",
            teclado
        )

    elif query.data == "RETOMAR":

        teclado = InlineKeyboardMarkup([
            [InlineKeyboardButton("🆘 Entre em contato com o suporte", url="https://t.me/infaedufilialbr?text=Quero%20retomar%20meus%20estudos!%20Meu%20curso%20%C3%A9%20INSIRA%20O%20CURSO%20e%20minha%20matr%C3%ADcula%20%C3%A9%20INSIRA%20A%20MATR%C3%8DCULA")],
            [InlineKeyboardButton("🏠 Voltar ao início", callback_data="INICIO")]
        ])

        await editar_tela(
            query,
            "imagens/inicio.jpg",
            "🔄 Retomar Estudos\n\nTenha em mãos o nome do curso para retomada e o número da sua matrícula.",
            teclado
        )

    elif query.data == "DUVIDAS":

        teclado = InlineKeyboardMarkup([
            [InlineKeyboardButton("🆘 Entre em contato com o suporte", url="https://t.me/infaedufilialbr?text=Ol%C3%A1%2C%20gostaria%20de%20tirar%20d%C3%BAvidas%20referente%20as%20qualifica%C3%A7%C3%B5es")],
            [InlineKeyboardButton("🏠 Voltar ao início", callback_data="INICIO")]
        ])

        await editar_tela(
            query,
            "imagens/inicio.jpg",
            "❓ Dúvidas\n\nPara retirar suas dúvidas, entre em contato direto com o nosso suporte.",
            teclado
        )
# -----------------------------
# MAIN
# -----------------------------
def main():

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(callbacks))

    print("Bot iniciado!")
    app.run_polling()


if __name__ == "__main__":
    main()