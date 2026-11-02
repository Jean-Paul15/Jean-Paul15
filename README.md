<div align="center">

<img src="assets/banner.svg" alt="Jean-Paul ADOGLI, ingénieur IA et Big Data" width="100%"/>

<p>
  <a href="https://www.linkedin.com/in/jean-paul-adogli-7203112b9"><img src="https://img.shields.io/badge/LinkedIn-Jean--Paul%20ADOGLI-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
  <a href="mailto:adoglijeanpaul@gmail.com"><img src="https://img.shields.io/badge/Email-adoglijeanpaul%40gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/></a>
  <a href="https://steko.app"><img src="https://img.shields.io/badge/Steko-steko.app-1d2a5b?style=for-the-badge" alt="Steko"/></a>
</p>

</div>

## En bref

Je construis des systèmes qui vont **de la collecte à la décision** : pipelines Kafka et Spark, modèles exposés par API, agents LLM avec RAG, le tout supervisé pour qu'on comprenne leur état d'un coup d'œil. J'aime les problèmes concrets qui doivent tenir en conditions réelles : la fraude, le crédit, le recrutement, l'industrie.

## De la donnée brute à la décision

```mermaid
flowchart LR
    A[Collecte<br/>Kafka · Airflow] --> B[Traitement<br/>Spark · lac de données]
    B --> C[Modèles<br/>LightGBM · autoencodeurs · LLM + RAG]
    C --> D[API<br/>FastAPI]
    D --> E[Supervision<br/>Prometheus · Grafana]
    E -. retour .-> A
```

## Projets phares

<table>
<tr>
<td width="50%" valign="top">

### [Détection de fraude en temps réel](https://github.com/Jean-Paul15/fraud-detection-paylink-africa)
La fraude pèse 0,15 % des transactions : un modèle naïf peut l'ignorer sans jamais se tromper. Quatre détecteurs de natures différentes, un méta-modèle, une validation par découpage temporel et un seuil guidé par le coût métier, exposés par une API de scoring.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white) ![LightGBM](https://img.shields.io/badge/LightGBM-02A676?style=flat-square) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)

</td>
<td width="50%" valign="top">

### [TalentFlow](https://github.com/Jean-Paul15/talentflow)
Des milliers d'offres d'emploi éparpillées sur le web, des CV à rapprocher : collecte, lac de données, recherche vectorielle, et une analyse des écarts de compétences expliquée par un LLM, sous supervision continue, jusqu'à l'application mobile.

![Kafka](https://img.shields.io/badge/Kafka-231F20?style=flat-square&logo=apachekafka&logoColor=white) ![Spark](https://img.shields.io/badge/Spark-E25A1C?style=flat-square&logo=apachespark&logoColor=white) ![Airflow](https://img.shields.io/badge/Airflow-017CEE?style=flat-square&logo=apacheairflow&logoColor=white) ![Qdrant](https://img.shields.io/badge/Qdrant-DC244C?style=flat-square&logo=qdrant&logoColor=white) ![Flutter](https://img.shields.io/badge/Flutter-02569B?style=flat-square&logo=flutter&logoColor=white)

</td>
</tr>
<tr>
<td width="50%" valign="top">

### [SOLIDA](https://github.com/Jean-Paul15/SOLIDA)
Noter un emprunteur qui n'a presque aucun papier. Un score fondé sur la trajectoire d'épargne, une couche solidaire pour le crédit de groupe, une décision proposée sous contrôle humain et consignée dans un journal qu'on ne peut pas réécrire.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white) ![Next.js](https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)

</td>
<td width="50%" valign="top">

### [Alerte précoce de crédit, zone UMOA](https://github.com/Jean-Paul15/ews-credit-umoa)
Repérer les crédits qui vont basculer en défaut trois mois avant l'incident, sur un portefeuille que personne n'a le droit de publier : le secret bancaire impose de le fabriquer.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![Spark](https://img.shields.io/badge/Spark-E25A1C?style=flat-square&logo=apachespark&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)

</td>
</tr>
<tr>
<td width="50%" valign="top">

### [Provisionnement IFRS 9 lisible](https://github.com/Jean-Paul15/credit-scoring)
Une probabilité de défaut que l'on peut lire, contrôler et défendre. Explainable Boosting Machine, contraintes de monotonie, scénarios macro, et une API qui renvoie la contribution exacte de chaque terme, sans boîte noire.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white) ![MLflow](https://img.shields.io/badge/MLflow-0194E2?style=flat-square&logo=mlflow&logoColor=white) ![DVC](https://img.shields.io/badge/DVC-945DD6?style=flat-square&logo=dvc&logoColor=white) ![Grafana](https://img.shields.io/badge/Grafana-F46800?style=flat-square&logo=grafana&logoColor=white)

</td>
<td width="50%" valign="top">

### [Pipeline de streaming temps réel](https://github.com/Jean-Paul15/kafka-spark-pipeline)
Des événements e-commerce, taxi, météo et immobiliers qui circulent de Kafka vers Spark, puis vers PostgreSQL, HDFS, Redis, Grafana, Superset et Streamlit. Une pile entière, démarrée par Docker Compose.

![Kafka](https://img.shields.io/badge/Kafka-231F20?style=flat-square&logo=apachekafka&logoColor=white) ![Spark](https://img.shields.io/badge/Spark-E25A1C?style=flat-square&logo=apachespark&logoColor=white) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white) ![Grafana](https://img.shields.io/badge/Grafana-F46800?style=flat-square&logo=grafana&logoColor=white)

</td>
</tr>
<tr>
<td width="50%" valign="top">

### [Base de données à la demande](https://github.com/Jean-Paul15/cloud-platform)
Un utilisateur s'authentifie, déclare un projet et réclame une instance MongoDB. Tout passe par une seule porte HTTPS, devant un cluster shardé isolé par trois réseaux Docker cloisonnés.

![Node.js](https://img.shields.io/badge/Node.js-5FA04E?style=flat-square&logo=nodedotjs&logoColor=white) ![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=flat-square&logo=mongodb&logoColor=white) ![Nginx](https://img.shields.io/badge/Nginx-009639?style=flat-square&logo=nginx&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)

</td>
<td width="50%" valign="top">

### [EpiGraph](https://github.com/Jean-Paul15/epigraph)
Qui a contaminé qui, où, et quel hôpital a fini par en payer le prix ? Les chaînes d'infection suivies comme un graphe Neo4j, de la simulation des données jusqu'au tableau de bord.

![Neo4j](https://img.shields.io/badge/Neo4j-4581C3?style=flat-square&logo=neo4j&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)

</td>
</tr>
</table>

**Et aussi :** [`ceng`](https://github.com/Jean-Paul15/claude-eng-framework), un orchestrateur déterministe en TypeScript qui retire du LLM les décisions qu'il prend mal sur un chantier long · [`ds-finance-quant`](https://github.com/Jean-Paul15/ds-finance-quant), quatre chaînes de risque bancaire de bout en bout · [`mobile-money-fraud`](https://github.com/Jean-Paul15/mobile-money-fraud), un service qui note et explique chaque transaction.

## Sous le capot

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

## Ma boîte à outils

<div align="center">

**IA et données**

<img src="https://skillicons.dev/icons?i=python,tensorflow,sklearn&perline=3" alt="Python, TensorFlow, scikit-learn"/>

![pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white) ![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white) ![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white) ![RAG](https://img.shields.io/badge/RAG-Qdrant%20%C2%B7%20ChromaDB-DC244C?style=for-the-badge) ![vLLM](https://img.shields.io/badge/vLLM-30A2FF?style=for-the-badge) ![Gemini](https://img.shields.io/badge/Gemini-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white) ![DeepSeek](https://img.shields.io/badge/DeepSeek-4D6BFE?style=for-the-badge)

**Big data et backend**

<img src="https://skillicons.dev/icons?i=kafka,fastapi,go,postgres,mongodb,supabase,redis&perline=7" alt="Kafka, FastAPI, Go, PostgreSQL, MongoDB, Supabase, Redis"/>

![Apache Spark](https://img.shields.io/badge/Apache%20Spark-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white) ![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-017CEE?style=for-the-badge&logo=apacheairflow&logoColor=white) ![Hadoop](https://img.shields.io/badge/Hadoop-66CCFF?style=for-the-badge&logo=apachehadoop&logoColor=black) ![MinIO](https://img.shields.io/badge/MinIO-C72E49?style=for-the-badge&logo=minio&logoColor=white) ![Traefik](https://img.shields.io/badge/Traefik-24A1C1?style=for-the-badge&logo=traefikproxy&logoColor=white)

**DevOps et cloud**

<img src="https://skillicons.dev/icons?i=docker,aws,grafana,prometheus,nginx,linux,git,github,githubactions&perline=9" alt="Docker, AWS, Grafana, Prometheus, Nginx, Linux, Git, GitHub, GitHub Actions"/>

**Développement web et mobile**

<img src="https://skillicons.dev/icons?i=nextjs,react,ts,tailwind,flutter,dart,nodejs&perline=7" alt="Next.js, React, TypeScript, Tailwind, Flutter, Dart, Node.js"/>

![Claude Code](https://img.shields.io/badge/Claude%20Code-D97757?style=for-the-badge&logo=claude&logoColor=white) ![Codex](https://img.shields.io/badge/Codex-412991?style=for-the-badge&logo=openai&logoColor=white)

**Analyse et visualisation**

![Looker Studio](https://img.shields.io/badge/Looker%20Studio-4285F4?style=for-the-badge&logo=looker&logoColor=white) ![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black) ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white) ![Superset](https://img.shields.io/badge/Superset-20A6C9?style=for-the-badge&logo=apachesuperset&logoColor=white)

</div>

## Certifications

**[Data Science Application](https://www.credly.com/badges/5887776b-4adc-4db7-bb95-f9b74d69e69b)** · WorldQuant University, août 2026  
Programme appliqué de huit projets en data science et machine learning : Random Forest et Gradient Boosting sur données déséquilibrées, segmentation K-means avec tableaux de bord Dash interactifs, tests A/B par chi-deux, modélisation de volatilité GARCH(1,1) en développement piloté par les tests. Des pipelines reproductibles, prêts à être déployés, et des résultats traduits en décisions métier.

**[Data Science Modeling](https://www.credly.com/badges/58558de1-639d-4dad-9934-7f457f8aaf22)** · WorldQuant University, août 2026  
Le cycle complet de la data science sur quatre projets pratiques (CSV, SQLite, MongoDB) : nettoyage et exploration de données tabulaires, analyse de corrélation, régression et classification supervisées avec régularisation Ridge et Lasso, modèles AR et ARMA, prévision de séries temporelles.

**[AWS Solutions Architect Associate SAA-C03](https://www.udemy.com/certificate/UC-5bca1f5c-cedd-4935-874a-c29a7696e51d/)** · Udemy, septembre 2026  
Préparation à l'examen AWS Certified Solutions Architect Associate : 43 heures de formation, 425 leçons, labs dans la console AWS, projets dans un compte AWS et 130 questions de révision, par un ancien architecte d'Amazon Web Services. Au programme, le Well-Architected Framework, IAM, EC2, le réseau, le stockage, les bases de données, l'analytique et les services d'IA, pour concevoir des architectures sécurisées, résilientes, performantes et maîtrisées en coût.

**[Data Science et Machine Learning avec Python](https://www.udemy.com/certificate/UC-c7343e22-1493-41be-a60f-bdba25c75ac3/)** · Udemy, décembre 2024  
Formation de 44,5 heures et 188 leçons, conçue avec Jose Portilla de Pierian Training : NumPy et Pandas pour manipuler des données réelles, visualisation avec Matplotlib et Seaborn, puis modèles de régression et de classification avec Scikit-Learn (régression linéaire et logistique, KNN, SVM, arbres de décision, Random Forests), préparation des variables, validation croisée et Grid Search. Des études de cas réels, à moitié théorie et à moitié code.

## Activité

<div align="center">

<img src="assets/activity.svg" alt="Activité GitHub : contributions, carte de chaleur et langages" width="100%"/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Jean-Paul15/Jean-Paul15/output/github-snake-dark.svg">
  <img alt="Le serpent mange mes contributions" src="https://raw.githubusercontent.com/Jean-Paul15/Jean-Paul15/output/github-snake.svg" width="95%"/>
</picture>

</div>

## En ce moment

Je construis **[Steko](https://steko.app)**, une application mobile de pilotage de vie dotée d'un agent d'IA : Flutter, Supabase et un moteur d'agent en Edge Functions. Elle est en test fermé sur Google Play. Je pousse aussi mes pipelines vers la supervision et l'évaluation des réponses d'IA, parce qu'une synthèse n'est utile que si elle est juste.

## Me contacter

Le plus simple : [LinkedIn](https://www.linkedin.com/in/jean-paul-adogli-7203112b9) ou par [e-mail](mailto:adoglijeanpaul@gmail.com).

<div align="center">
  <img src="assets/footer.svg" alt="" width="100%"/>
</div>
