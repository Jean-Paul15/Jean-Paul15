<div align="center">

<img src="assets/banner.svg" alt="Jean-Paul ADOGLI, ingénieur IA et Big Data" width="100%"/>

<p>
  <a href="https://www.linkedin.com/in/jean-paul-adogli-7203112b9"><img src="https://img.shields.io/badge/LinkedIn-Jean--Paul%20ADOGLI-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
  <a href="mailto:adoglijeanpaul@gmail.com"><img src="https://img.shields.io/badge/Email-adoglijeanpaul%40gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/></a>
  <a href="https://steko.app"><img src="https://img.shields.io/badge/Steko-steko.app-1d2a5b?style=for-the-badge" alt="Steko"/></a>
  <img src="https://komarev.com/ghpvc/?username=Jean-Paul15&label=Visites&color=2c5364&style=for-the-badge" alt="Visites du profil"/>
</p>

</div>

## <img src="https://api.iconify.design/lucide/user.svg?color=%2338bdf8" width="22" height="22" align="center" alt=""/> En bref

Je construis des systèmes qui vont **de la collecte à la décision** : pipelines Kafka et Spark, modèles exposés par API, agents LLM avec RAG, le tout supervisé pour qu'on comprenne leur état d'un coup d'œil. J'aime les problèmes concrets qui doivent tenir en conditions réelles : la fraude, le crédit, le recrutement, l'industrie.

## <img src="https://api.iconify.design/lucide/workflow.svg?color=%2338bdf8" width="22" height="22" align="center" alt=""/> De la donnée brute à la décision

```mermaid
flowchart LR
    A[Collecte<br/>Kafka · Airflow] --> B[Traitement<br/>Spark · lac de données]
    B --> C[Modèles<br/>LightGBM · autoencodeurs · LLM + RAG]
    C --> D[API<br/>FastAPI]
    D --> E[Supervision<br/>Prometheus · Grafana]
    E -. retour .-> A
```

## <img src="https://api.iconify.design/lucide/layers.svg?color=%2338bdf8" width="22" height="22" align="center" alt=""/> Projets phares

<table>
<tr>
<td width="50%" valign="top">

### <img src="https://api.iconify.design/lucide/shield-check.svg?color=%2338bdf8" width="20" height="20" align="center" alt=""/> [Détection de fraude en temps réel](https://github.com/Jean-Paul15/fraud-detection-paylink-africa)
La fraude pèse 0,15 % des transactions : un modèle naïf peut l'ignorer sans jamais se tromper. Quatre détecteurs de natures différentes, un méta-modèle, une validation par découpage temporel et un seuil guidé par le coût métier, exposés par une API de scoring.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white) ![LightGBM](https://img.shields.io/badge/LightGBM-02A676?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)

</td>
<td width="50%" valign="top">

### <img src="https://api.iconify.design/lucide/search.svg?color=%2338bdf8" width="20" height="20" align="center" alt=""/> [TalentFlow](https://github.com/Jean-Paul15/talentflow)
Des milliers d'offres d'emploi éparpillées sur le web, des CV à rapprocher : collecte, lac de données, recherche vectorielle, et une analyse des écarts de compétences expliquée par un LLM, sous supervision continue, jusqu'à l'application mobile.

![Kafka](https://img.shields.io/badge/Kafka-231F20?style=flat-square&logo=apachekafka&logoColor=white) ![Spark](https://img.shields.io/badge/Spark-E25A1C?style=flat-square&logo=apachespark&logoColor=white) ![Airflow](https://img.shields.io/badge/Airflow-017CEE?style=flat-square&logo=apacheairflow&logoColor=white) ![Qdrant](https://img.shields.io/badge/Qdrant-DC244C?style=flat-square&logo=qdrant&logoColor=white) ![Flutter](https://img.shields.io/badge/Flutter-02569B?style=flat-square&logo=flutter&logoColor=white)

</td>
</tr>
<tr>
<td width="50%" valign="top">

### <img src="https://api.iconify.design/lucide/handshake.svg?color=%2338bdf8" width="20" height="20" align="center" alt=""/> [SOLIDA](https://github.com/Jean-Paul15/SOLIDA)
Noter un emprunteur qui n'a presque aucun papier. Un score fondé sur la trajectoire d'épargne, une couche solidaire pour le crédit de groupe, une décision proposée sous contrôle humain et consignée dans un journal qu'on ne peut pas réécrire.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white) ![Next.js](https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)

</td>
<td width="50%" valign="top">

### <img src="https://api.iconify.design/lucide/bell-ring.svg?color=%2338bdf8" width="20" height="20" align="center" alt=""/> [Alerte précoce de crédit, zone UMOA](https://github.com/Jean-Paul15/ews-credit-umoa)
Repérer les crédits qui vont basculer en défaut trois mois avant l'incident, sur un portefeuille que personne n'a le droit de publier : le secret bancaire impose de le fabriquer.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![Spark](https://img.shields.io/badge/Spark-E25A1C?style=flat-square&logo=apachespark&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)

</td>
</tr>
<tr>
<td width="50%" valign="top">

### <img src="https://api.iconify.design/lucide/calculator.svg?color=%2338bdf8" width="20" height="20" align="center" alt=""/> [Provisionnement IFRS 9 lisible](https://github.com/Jean-Paul15/credit-scoring)
Une probabilité de défaut que l'on peut lire, contrôler et défendre. Explainable Boosting Machine, contraintes de monotonie, scénarios macro, et une API qui renvoie la contribution exacte de chaque terme, sans boîte noire.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white) ![MLflow](https://img.shields.io/badge/MLflow-0194E2?style=flat-square&logo=mlflow&logoColor=white) ![DVC](https://img.shields.io/badge/DVC-945DD6?style=flat-square&logo=dvc&logoColor=white) ![Grafana](https://img.shields.io/badge/Grafana-F46800?style=flat-square&logo=grafana&logoColor=white)

</td>
<td width="50%" valign="top">

### <img src="https://api.iconify.design/lucide/waves.svg?color=%2338bdf8" width="20" height="20" align="center" alt=""/> [Pipeline de streaming temps réel](https://github.com/Jean-Paul15/kafka-spark-pipeline)
Des événements e-commerce, taxi, météo et immobiliers qui circulent de Kafka vers Spark, puis vers PostgreSQL, HDFS, Redis, Grafana, Superset et Streamlit. Une pile entière, démarrée par Docker Compose.

![Kafka](https://img.shields.io/badge/Kafka-231F20?style=flat-square&logo=apachekafka&logoColor=white) ![Spark](https://img.shields.io/badge/Spark-E25A1C?style=flat-square&logo=apachespark&logoColor=white) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white) ![Grafana](https://img.shields.io/badge/Grafana-F46800?style=flat-square&logo=grafana&logoColor=white)

</td>
</tr>
<tr>
<td width="50%" valign="top">

### <img src="https://api.iconify.design/lucide/cloud.svg?color=%2338bdf8" width="20" height="20" align="center" alt=""/> [Base de données à la demande](https://github.com/Jean-Paul15/cloud-platform)
Un utilisateur s'authentifie, déclare un projet et réclame une instance MongoDB. Tout passe par une seule porte HTTPS, devant un cluster shardé isolé par trois réseaux Docker cloisonnés.

![Node.js](https://img.shields.io/badge/Node.js-5FA04E?style=flat-square&logo=nodedotjs&logoColor=white) ![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=flat-square&logo=mongodb&logoColor=white) ![Nginx](https://img.shields.io/badge/Nginx-009639?style=flat-square&logo=nginx&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)

</td>
<td width="50%" valign="top">

### <img src="https://api.iconify.design/lucide/share-2.svg?color=%2338bdf8" width="20" height="20" align="center" alt=""/> [EpiGraph](https://github.com/Jean-Paul15/epigraph)
Qui a contaminé qui, où, et quel hôpital a fini par en payer le prix ? Les chaînes d'infection suivies comme un graphe Neo4j, de la simulation des données jusqu'au tableau de bord.

![Neo4j](https://img.shields.io/badge/Neo4j-4581C3?style=flat-square&logo=neo4j&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)

</td>
</tr>
</table>

**Et aussi :** [`ceng`](https://github.com/Jean-Paul15/claude-eng-framework), un orchestrateur déterministe en TypeScript qui retire du LLM les décisions qu'il prend mal sur un chantier long · [`ds-finance-quant`](https://github.com/Jean-Paul15/ds-finance-quant), quatre chaînes de risque bancaire de bout en bout · [`mobile-money-fraud`](https://github.com/Jean-Paul15/mobile-money-fraud), un service qui note et explique chaque transaction.

## <img src="https://api.iconify.design/lucide/cpu.svg?color=%2338bdf8" width="22" height="22" align="center" alt=""/> Sous le capot

Ce qui m'intéresse, ce sont les décisions d'ingénierie qui font qu'un système reste juste et tient en production.

<details>
<summary><b>Une évaluation sans fuite temporelle</b></summary>

Dans la détection de fraude, le jeu est coupé à une date fixe avant tout calcul de variables. Les moyennes par émetteur sont apprises sur l'entraînement puis réutilisées telles quelles sur le test, et la fenêtre glissante de 24 heures exclut la transaction courante. Un score qui triche en regardant l'avenir ne vaut rien en production.

</details>

<details>
<summary><b>Un modèle de crédit qu'on peut défendre</b></summary>

La probabilité de défaut est une Explainable Boosting Machine : l'API renvoie la contribution exacte de chaque terme, sans SHAP. Des contraintes de monotonie sont posées sur le retard, le ratio de service de la dette et la couverture par garantie. Les variables issues du graphe de transactions sont exclues des modèles éligibles, car elles ne sont pas point-in-time.

</details>

<details>
<summary><b>Une plateforme cloisonnée par conception</b></summary>

Trois réseaux Docker : seul Nginx touche le réseau public, les deux autres sont déclarés internes et n'ont aucune sortie directe vers l'extérieur. L'authentification fait tourner ses jetons : chaque rafraîchissement supprime l'ancien et en émet un nouveau. Derrière, un cluster MongoDB shardé démarré par script.

```mermaid
flowchart LR
    U[Utilisateur] -->|HTTPS| N[Nginx<br/>réseau public]
    N --> S[Services auth et gestion<br/>réseau privé interne]
    S --> M[Cluster MongoDB shardé<br/>réseau de données interne]
```

</details>

<details>
<summary><b>Une décision de crédit sous contrôle humain</b></summary>

Pour un emprunteur sans papiers, SOLIDA propose une décision avec les facteurs qui l'expliquent, mais c'est un humain qui tranche, et chaque décision est consignée dans un journal qu'on ne peut pas réécrire.

</details>

## <img src="https://api.iconify.design/lucide/wrench.svg?color=%2338bdf8" width="22" height="22" align="center" alt=""/> Ma boîte à outils

<div align="center">

**IA et données**

<img src="https://skillicons.dev/icons?i=python,tensorflow,sklearn,pandas,numpy,jupyter&perline=6" alt="Python, TensorFlow, scikit-learn, pandas, NumPy, Jupyter"/>

![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white) ![RAG](https://img.shields.io/badge/RAG-Qdrant%20%C2%B7%20ChromaDB-DC244C?style=for-the-badge) ![vLLM](https://img.shields.io/badge/vLLM-30A2FF?style=for-the-badge) ![Gemini](https://img.shields.io/badge/Gemini-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white) ![DeepSeek](https://img.shields.io/badge/DeepSeek-4D6BFE?style=for-the-badge)

**Big data et backend**

<img src="https://skillicons.dev/icons?i=kafka,spark,airflow,hadoop,fastapi,go,postgres,mongodb,supabase,redis&perline=10" alt="Kafka, Spark, Airflow, Hadoop, FastAPI, Go, PostgreSQL, MongoDB, Supabase, Redis"/>

**DevOps et cloud**

<img src="https://skillicons.dev/icons?i=docker,aws,grafana,prometheus,nginx,linux,git,github,githubactions&perline=9" alt="Docker, AWS, Grafana, Prometheus, Nginx, Linux, Git, GitHub, GitHub Actions"/>

**Développement web et mobile**

<img src="https://skillicons.dev/icons?i=nextjs,react,ts,tailwind,flutter,dart,nodejs&perline=7" alt="Next.js, React, TypeScript, Tailwind, Flutter, Dart, Node.js"/>

![Claude Code](https://img.shields.io/badge/Claude%20Code-D97757?style=for-the-badge&logo=claude&logoColor=white) ![Codex](https://img.shields.io/badge/Codex-412991?style=for-the-badge&logo=openai&logoColor=white)

**Analyse et visualisation**

![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black) ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white) ![Superset](https://img.shields.io/badge/Superset-20A6C9?style=for-the-badge&logo=apachesuperset&logoColor=white)

</div>

## <img src="https://api.iconify.design/lucide/activity.svg?color=%2338bdf8" width="22" height="22" align="center" alt=""/> Activité

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api?username=Jean-Paul15&show_icons=true&theme=tokyonight&hide_border=true&count_private=true&include_all_commits=true&rank_icon=github">
  <img alt="Statistiques GitHub" src="https://github-readme-stats.vercel.app/api?username=Jean-Paul15&show_icons=true&theme=default&hide_border=true&count_private=true&include_all_commits=true&rank_icon=github" height="170"/>
</picture>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api/top-langs/?username=Jean-Paul15&layout=compact&theme=tokyonight&hide_border=true&langs_count=8">
  <img alt="Langages les plus utilisés" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Jean-Paul15&layout=compact&theme=default&hide_border=true&langs_count=8" height="170"/>
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://streak-stats.demolab.com?user=Jean-Paul15&theme=tokyonight&hide_border=true&locale=fr">
  <img alt="Série de contributions" src="https://streak-stats.demolab.com?user=Jean-Paul15&theme=default&hide_border=true&locale=fr" width="95%"/>
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-activity-graph.vercel.app/graph?username=Jean-Paul15&theme=tokyo-night&hide_border=true&area=true&custom_title=Contributions%20des%2030%20derniers%20jours">
  <img alt="Graphe d'activité" src="https://github-readme-activity-graph.vercel.app/graph?username=Jean-Paul15&theme=minimal&hide_border=true&area=true&custom_title=Contributions%20des%2030%20derniers%20jours" width="95%"/>
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Jean-Paul15/Jean-Paul15/output/github-snake-dark.svg">
  <img alt="Le serpent mange mes contributions" src="https://raw.githubusercontent.com/Jean-Paul15/Jean-Paul15/output/github-snake.svg" width="95%"/>
</picture>

</div>

## <img src="https://api.iconify.design/lucide/rocket.svg?color=%2338bdf8" width="22" height="22" align="center" alt=""/> En ce moment

Je construis **[Steko](https://steko.app)**, une application mobile de pilotage de vie dotée d'un agent d'IA : Flutter, Supabase et un moteur d'agent en Edge Functions. Elle est en test fermé sur Google Play. Je pousse aussi mes pipelines vers la supervision et l'évaluation des réponses d'IA, parce qu'une synthèse n'est utile que si elle est juste.

## <img src="https://api.iconify.design/lucide/mail.svg?color=%2338bdf8" width="22" height="22" align="center" alt=""/> Me contacter

Le plus simple : [LinkedIn](https://www.linkedin.com/in/jean-paul-adogli-7203112b9) ou par [e-mail](mailto:adoglijeanpaul@gmail.com).

<div align="center">
  <img src="assets/footer.svg" alt="" width="100%"/>
</div>
