<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f2027,50:203a43,100:2c5364&height=210&section=header&text=Jean-Paul%20ADOGLI&fontSize=52&fontColor=ffffff&fontAlignY=38&desc=Ing%C3%A9nieur%20IA%20%26%20Big%20Data&descSize=22&descAlignY=60&animation=fadeIn" alt="Jean-Paul ADOGLI, ingénieur IA et Big Data" width="100%"/>

<a href="https://github.com/Jean-Paul15">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=21&duration=3200&pause=900&color=38BDF8&center=true&vCenter=true&width=720&lines=Je+construis+des+syst%C3%A8mes+qui+vont+de+la+donn%C3%A9e+%C3%A0+la+d%C3%A9cision;Pipelines+Kafka+%2B+Spark%2C+mod%C3%A8les+expos%C3%A9s+par+API;Agents+LLM%2C+RAG+et+supervision+Prometheus+%2B+Grafana" alt="Animation de présentation" />
</a>

<p>
  <a href="https://www.linkedin.com/in/jean-paul-adogli-7203112b9"><img src="https://img.shields.io/badge/LinkedIn-Jean--Paul%20ADOGLI-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
  <a href="mailto:adoglijeanpaul@gmail.com"><img src="https://img.shields.io/badge/Email-adoglijeanpaul%40gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/></a>
  <a href="https://steko.app"><img src="https://img.shields.io/badge/Steko-steko.app-1d2a5b?style=for-the-badge" alt="Steko"/></a>
  <img src="https://komarev.com/ghpvc/?username=Jean-Paul15&label=Visites&color=2c5364&style=for-the-badge" alt="Visites du profil"/>
</p>

</div>

## 👋 En bref

Passionné par la donnée depuis la deuxième année de licence, je construis des systèmes qui vont **de la collecte à la décision** : pipelines Kafka et Spark, modèles exposés par API, agents LLM avec RAG, le tout supervisé pour qu'on comprenne leur état d'un coup d'œil. J'aime les problèmes concrets qui doivent tenir en conditions réelles, de la fraude au crédit, du recrutement à l'industrie.

## 🧭 De la donnée brute à la décision

```mermaid
flowchart LR
    A[Collecte<br/>Kafka · Airflow] --> B[Traitement<br/>Spark · lac de données]
    B --> C[Modèles<br/>LightGBM · autoencodeurs · LLM + RAG]
    C --> D[API<br/>FastAPI]
    D --> E[Supervision<br/>Prometheus · Grafana]
    E -. retour .-> A
```

## 🚀 Projets phares

<table>
<tr>
<td width="50%" valign="top">

### 🛡️ [Détection de fraude en temps réel](https://github.com/Jean-Paul15/fraud-detection-paylink-africa)
La fraude pèse 0,15 % des transactions : un modèle naïf peut l'ignorer sans jamais se tromper. Quatre détecteurs de natures différentes, un méta-modèle, une validation par découpage temporel et un seuil guidé par le coût métier, exposés par une API de scoring.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white) ![LightGBM](https://img.shields.io/badge/LightGBM-02A676?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)

</td>
<td width="50%" valign="top">

### 🧲 [TalentFlow](https://github.com/Jean-Paul15/talentflow)
Des milliers d'offres d'emploi éparpillées sur le web, des CV à rapprocher : collecte, lac de données, recherche vectorielle, et une analyse des écarts de compétences expliquée par un LLM, sous supervision continue, jusqu'à l'application mobile.

![Kafka](https://img.shields.io/badge/Kafka-231F20?style=flat-square&logo=apachekafka&logoColor=white) ![Spark](https://img.shields.io/badge/Spark-E25A1C?style=flat-square&logo=apachespark&logoColor=white) ![Airflow](https://img.shields.io/badge/Airflow-017CEE?style=flat-square&logo=apacheairflow&logoColor=white) ![Qdrant](https://img.shields.io/badge/Qdrant-DC244C?style=flat-square&logo=qdrant&logoColor=white) ![Flutter](https://img.shields.io/badge/Flutter-02569B?style=flat-square&logo=flutter&logoColor=white)

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🤝 [SOLIDA](https://github.com/Jean-Paul15/SOLIDA)
Noter un emprunteur qui n'a presque aucun papier. Un score fondé sur la trajectoire d'épargne, une couche solidaire pour le crédit de groupe, une décision proposée sous contrôle humain et consignée dans un journal infalsifiable.
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white) ![Next.js](https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)

</td>
<td width="50%" valign="top">

### 📉 [Alerte précoce de crédit, zone UMOA](https://github.com/Jean-Paul15/ews-credit-umoa)
Repérer les crédits qui vont basculer en défaut trois mois avant l'incident, sur un portefeuille que personne n'a le droit de publier : le secret bancaire impose de le fabriquer.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![Spark](https://img.shields.io/badge/Spark-E25A1C?style=flat-square&logo=apachespark&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 📊 [Provisionnement IFRS 9 lisible](https://github.com/Jean-Paul15/credit-scoring)
Une probabilité de défaut que l'on peut lire, contrôler et défendre. Explainable Boosting Machine, contraintes de monotonie, scénarios macro, et une API qui renvoie la contribution exacte de chaque terme, sans boîte noire.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white) ![MLflow](https://img.shields.io/badge/MLflow-0194E2?style=flat-square&logo=mlflow&logoColor=white) ![DVC](https://img.shields.io/badge/DVC-945DD6?style=flat-square&logo=dvc&logoColor=white) ![Grafana](https://img.shields.io/badge/Grafana-F46800?style=flat-square&logo=grafana&logoColor=white)

</td>
<td width="50%" valign="top">

### 🌊 [Pipeline de streaming temps réel](https://github.com/Jean-Paul15/kafka-spark-pipeline)
Des événements e-commerce, taxi, météo et immobiliers qui circulent de Kafka vers Spark, puis vers PostgreSQL, HDFS, Redis, Grafana, Superset et Streamlit. Une pile entière, démarrée par Docker Compose.

![Kafka](https://img.shields.io/badge/Kafka-231F20?style=flat-square&logo=apachekafka&logoColor=white) ![Spark](https://img.shields.io/badge/Spark-E25A1C?style=flat-square&logo=apachespark&logoColor=white) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white) ![Grafana](https://img.shields.io/badge/Grafana-F46800?style=flat-square&logo=grafana&logoColor=white)

</td>
</tr>
<tr>
<td width="50%" valign="top">

### ☁️ [Base de données à la demande](https://github.com/Jean-Paul15/cloud-platform)
Un utilisateur s'authentifie, déclare un projet et réclame une instance MongoDB. Tout passe par une seule porte HTTPS, devant un cluster shardé isolé par trois réseaux Docker cloisonnés.

![Node.js](https://img.shields.io/badge/Node.js-5FA04E?style=flat-square&logo=nodedotjs&logoColor=white) ![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=flat-square&logo=mongodb&logoColor=white) ![Nginx](https://img.shields.io/badge/Nginx-009639?style=flat-square&logo=nginx&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)

</td>
<td width="50%" valign="top">

### 🦠 [EpiGraph](https://github.com/Jean-Paul15/epigraph)
Qui a contaminé qui, où, et quel hôpital a fini par en payer le prix ? Les chaînes d'infection suivies comme un graphe Neo4j, de la simulation des données jusqu'au tableau de bord.

![Neo4j](https://img.shields.io/badge/Neo4j-4581C3?style=flat-square&logo=neo4j&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)

</td>
</tr>
</table>

**Et aussi :** [`ceng`](https://github.com/Jean-Paul15/claude-eng-framework), un orchestrateur déterministe en TypeScript qui retire du LLM les décisions qu'il prend mal sur un chantier long · [`ds-finance-quant`](https://github.com/Jean-Paul15/ds-finance-quant), quatre chaînes de risque bancaire de bout en bout · [`mobile-money-fraud`](https://github.com/Jean-Paul15/mobile-money-fraud), un service qui note et explique chaque transaction.

## 🧰 Ma boîte à outils

<div align="center">

**IA et données**

<img src="https://skillicons.dev/icons?i=python,tensorflow,sklearn,pandas,numpy,jupyter&perline=6" alt="Python, TensorFlow, scikit-learn, pandas, NumPy, Jupyter"/>

![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white) ![RAG](https://img.shields.io/badge/RAG-Qdrant%20%C2%B7%20ChromaDB-DC244C?style=for-the-badge) ![vLLM](https://img.shields.io/badge/vLLM-LLM%20auto--h%C3%A9berg%C3%A9s-30A2FF?style=for-the-badge) ![Gemini](https://img.shields.io/badge/Gemini-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white) ![DeepSeek](https://img.shields.io/badge/DeepSeek-4D6BFE?style=for-the-badge) ![Claude](https://img.shields.io/badge/Claude-D97757?style=for-the-badge&logo=claude&logoColor=white)

**Big data et backend**

<img src="https://skillicons.dev/icons?i=kafka,spark,airflow,hadoop,fastapi,go,postgres,mongodb,supabase,redis&perline=10" alt="Kafka, Spark, Airflow, Hadoop, FastAPI, Go, PostgreSQL, MongoDB, Supabase, Redis"/>

**DevOps et cloud**

<img src="https://skillicons.dev/icons?i=docker,aws,grafana,prometheus,nginx,linux,git,github,githubactions&perline=9" alt="Docker, AWS, Grafana, Prometheus, Nginx, Linux, Git, GitHub, GitHub Actions"/>

**Web et mobile**

<img src="https://skillicons.dev/icons?i=nextjs,react,ts,tailwind,flutter,dart,nodejs&perline=7" alt="Next.js, React, TypeScript, Tailwind, Flutter, Dart, Node.js"/>

**Analyse et visualisation**

![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black) ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white) ![Superset](https://img.shields.io/badge/Superset-20A6C9?style=for-the-badge&logo=apachesuperset&logoColor=white)

</div>

## 📈 Activité

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

## 🔭 En ce moment

- 🚧 Je construis **[Steko](https://steko.app)**, une application mobile de pilotage de vie dotée d'un agent d'IA : Flutter, Supabase et un moteur d'agent en Edge Functions. En test fermé sur Google Play.
- 🧪 Je pousse mes pipelines vers la **supervision et l'évaluation des réponses d'IA**, parce qu'une synthèse n'est utile que si elle est juste.

## 📬 Me contacter

Le plus simple : [LinkedIn](https://www.linkedin.com/in/jean-paul-adogli-7203112b9) ou par [e-mail](mailto:adoglijeanpaul@gmail.com).
<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:2c5364,50:203a43,100:0f2027&height=120&section=footer" alt="" width="100%"/>
</div>
