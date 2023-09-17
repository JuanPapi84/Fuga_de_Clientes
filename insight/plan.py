# %% [markdown]
# # Hola &#x1F600;
# 
# Soy **Hesus Garcia**, revisor de código de Triple Ten, y voy a examinar el proyecto que has desarrollado recientemente. Si encuentro algún error, te lo señalaré para que lo corrijas, ya que mi objetivo es ayudarte a prepararte para un ambiente de trabajo real, donde el líder de tu equipo actuaría de la misma manera. Si no puedes solucionar el problema, te proporcionaré más información en la próxima oportunidad. Cuando encuentres un comentario,  **por favor, no los muevas, no los modifiques ni los borres**. 
# 
# Revisaré cuidadosamente todas las implementaciones que has realizado para cumplir con los requisitos y te proporcionaré mis comentarios de la siguiente manera:
# 
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class=“tocSkip”></a>
# Si todo está perfecto.
# </div>
# 
# <div class="alert alert-block alert-warning">
# <b>Comentario del revisor</b> <a class=“tocSkip”></a>
# Si tu código está bien pero se puede mejorar o hay algún detalle que le hace falta.
# </div>
# 
# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class=“tocSkip”></a>
# Si de pronto hace falta algo o existe algún problema con tu código o conclusiones.
# </div>
# 
# Puedes responderme de esta forma:
# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class=“tocSkip”></a>
# </div>
# 
# </br>
# 
# **¡Empecemos!**  &#x1F680;
# 

# %% [markdown]
# # Proyecto Final Telefonica

# %% [markdown]
# Una Compañía de teléfonos está preocupada porque algunos de sus clientes se van, para ellos quieren saber si hay alguna forma de saber la razón de la terminación del contrato y me proporciono los `Datasets` de los contratos, los servicios de internet, los servicios de teléfonos y de las personas que viven en cada hogar. 

# %% [markdown]
# ## Indice

# %% [markdown]
# 1) Carga de Librerías 
# 
# 2) Carga de los datos 
# 
#     - DataFrame de Contratos 
# 
#     - DataFrame de Internet 
# 
#     - DataFrame de Personas 
# 
#     - DataFrame de Teléfonos 
# 
# 
# 3) EDA de los DataFrames 
# 
#     - Dtypes 
# 
#     - Gráficos 
# 
# 4) Conclusiones Parciales 
# 
#   
# 5) Recomendaciones 
# 
# 
# 6) Próximos Pasos 

# %% [markdown]
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class=“tocSkip”></a>
# Me parece genial que hayas incluido una tabla de contenidos en tu documento, esto facilitará la navegación y comprensión de los temas que estás tratando. ¡Sigue así!</div>
# </div>
# 

# %% [markdown]
# # 1 Carga de Librerías

# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os 



# %% [markdown]
# ## Carga de los Datos

# %% [markdown]
# ### DataFrame de Contratos

# %%
df_contratos  = pd.read_csv('files/datasets/input/contract.csv')

# %%

# %%
df_contratos

# %%


# %% [markdown]
# ### DataFrame de Internet

# %%
df_internet = pd.read_csv('internet.csv')

# %%
df_internet

# %% [markdown]
# ### DataFrame Personal

# %%
df_personal = pd.read_csv('personal.csv')

# %%
df_personal

# %% [markdown]
# ### DataFrame Telefono

# %%
df_phone = pd.read_csv('phone.csv')

# %%
df_phone

# %% [markdown]
# ##  EDA de los DataFrames

# %% [markdown]
# ### Diccionario de Contratos

# %% [markdown]
# Los datos contenido dentro de **contract.csv**:
# 
# - `costumerID` : Identificación del usuario.
# - `BeginDate`: Fecha de inicio de subscripción del usuario.
# - `EndDate` : Fecha de finalización de subscripción del usuario.
# - `Type` : Tipo de plan de pago con respecto al tiempo de renovación.
# - `PaperlessBilling` : Facturación digital.
# - `PaymentMethod` : Método de pago.
# - `MonthlyCharges` : Cargo mensual en USD.
# - `TotalCharges` : Cargo total en USD.

# %% [markdown]
# ### Dtypes Contratos

# %%
df_contratos.info()

# %%
# Convertir la columna TotalCharges a tipo numérico
df_contratos['TotalCharges'] = pd.to_numeric(df_contratos['TotalCharges'], errors='coerce')
print(df_contratos.dtypes)

# %%
# Suponiendo que 'df' es tu DataFrame
nan_count = df_contratos['TotalCharges'].isna().sum()

print("Número de valores NaN en TotalCharges:", nan_count)

# %% [markdown]
# <div class="alert alert-block alert-danger">
#     <b>Comentarios del Revisor</b> <a class="tocSkip"></a><br>
# Es importante considerar los valores ausentes que no están implicitos. En este caso si bien el valor no se interpreta como NaN, la variable TotalCharges tiene un 16% de valores ausentes, que encontrarás cuando cambies de tipo object a tipo númerico. Te aconsejo considerar esto para los otros data sets y plantearlo en tus conclusiones.
# </div>

# %% [markdown]
# Las columnas de las fechas estan como objetos, hay que cambiarlas a datetime64ns, hay valores ausentes en la columna `TotalCharges` tengo que calcular cuando fue que inicio su contrato y si lo finalizo o no y dependiendo de eso y del cargo mensual que tiene rellenar los valores ausentes.

# %%
df_contratos.describe()

# %% [markdown]
# ### Diccionario de Internet

# %% [markdown]
# Los datos contenido dentro de **internet.csv**:
# 
# - `costumerID` : Identificación del usuario.
# - `InternetService`: Subscripción del usuario al servicio de internet.
# - `OnlineSecurity` : Subscripción del usuario a la seguridad online.
# - `OnlineBackup` : Subscripción del usuario a recuperación de la información online.
# - `DeviceProtection` : Subscripción del usuario a protección del aparato.
# - `TechSupport` : Subscripción del usuario al soporte tecnico.
# - `StreamingTV` : Subscripción del usuario al servicio de televisión por internet.
# - `StreamingMovies` : Subscripción del usuario al servicio de peliculas en internet.

# %% [markdown]
# ### Dtype Internert

# %%
df_internet.info()

# %%
df_internet.describe()

# %% [markdown]
# Hay menos datos que el dataframe de contrato, pero no se ven valores ausentes, de los servicios de `InternerService` hay 3096 usuarios que la contrataron, en `OnlineSecurity` hay 3498 usuarios, `OnlineBackup` hay 3088, `DeviceProtection` hay 3095, `TechSupport` hay 3473, `StreamingTV` hay 2810 y en `StreamingMovies` hay 2785 usuarios suscriptos.

# %% [markdown]
# ### Diccionario de Personal

# %% [markdown]
# Los datos contenido dentro de **personal.csv**:
# 
# - `costumerID` : Identificación del usuario.
# - `gender`: Genero del titular.
# - `SeniorCitizen` : Pertenece a la 3ra edad.
# - `Partner` : Tiene pareja.
# - `Dependents` : Tiene personas a su cargo.

# %% [markdown]
# ### Dtype Personal

# %%
df_personal.info()

# %%
df_personal.describe()

# %% [markdown]
# Tampocos hay nulos

# %% [markdown]
# ### Diccionario Phone

# %% [markdown]
# Los datos contenido dentro de **phone.csv**:
# 
# - `costumerID` : Identificación del usuario.
# - `MultipleLines`: Posee mas de una linea telefonica.

# %% [markdown]
# ### Dtype Phone

# %%
df_phone.info()

# %%
df_phone.describe()

# %% [markdown]
# En el último dataframe vemos que tampoco hay datos nulos pero si menores datos que en el dataframe de contratos y personal

# %% [markdown]
# <div class="alert alert-block alert-warning">
#     <b>Comentarios del Revisor</b> <a class="tocSkip"></a><br>
# Correcto, info(), head()  son herramientas esceneciales que nos ayudaran a hacer un análisis exploratorio inicial. Opcionalmente podrías siempre incluir describe() para tener mejor idea de los valores que toman tus varibales. Continúa con el buen trabajo! </div>

# %% [markdown]
# <div class="alert alert-block alert-danger">
#     <b>Comentarios del Revisor</b> <a class="tocSkip"></a><br>
# Buen trabajo pero en esta sección sería importante incluir un breve diccionario de datos para cada conjunto. Por ejemplo: 
# <code>
# Los datos contenido dentro de **contract.csv**:
# 
# - `costumerID` : Identificación del usuario.
# - `BeginDate`: Fecha de inicio de subscripción del usuario.
# - `EndDate` : Fecha de finalización de subscripción del usuario.
# - `Type` : Tipo de plan de pago con respecto al tiempo de renovación.
# - `PaperlessBilling` : Facturación digital.
# - `PaymentMethod` : Método de pago.
# - `MonthlyCharges` : Cargo mensual en USD.
# - `TotalCharges` : Cargo total en USD.
# </code></div>

# %% [markdown]
# ## Gráficos
# 

# %% [markdown]
# ### Contratos

# %%
# Gráfico de barras para el tipo de contrato
contract_counts = df_contratos["Type"].value_counts()
plt.bar(contract_counts.index, contract_counts.values)
plt.title("Distribución de tipos de contrato")
plt.xlabel("Tipo de contrato")
plt.ylabel("Número de clientes")
plt.show()

# Histograma de Cargos Mensuales
plt.figure(figsize=(8, 6))
plt.hist(df_contratos['MonthlyCharges'], bins=20, color='skyblue', edgecolor='black')
plt.title('Histograma de Cargos Mensuales')
plt.xlabel('Cargos Mensuales')
plt.ylabel('Frecuencia')
plt.show()

# Histograma de Cargos Totales
plt.figure(figsize=(8, 6))
plt.hist(df_contratos['TotalCharges'], bins=20, color='lightgreen', edgecolor='black')
plt.title('Histograma de Cargos Totales')
plt.xlabel('Cargos Totales')
plt.ylabel('Frecuencia')
plt.show()

# Diagrama de dispersión entre Cargos Mensuales y Cargos Totales
plt.figure(figsize=(8, 6))
plt.scatter(df_contratos['MonthlyCharges'], df_contratos['TotalCharges'], alpha=0.5)
plt.title('Diagrama de Dispersión entre Cargos Mensuales y Cargos Totales')
plt.xlabel('Cargos Mensuales')
plt.ylabel('Cargos Totales')
plt.show()


# %%
# Histograma de Cargos Mensuales por Tipo de Pago
plt.figure(figsize=(10, 6))
sns.histplot(data=df_contratos, x='MonthlyCharges', hue='PaymentMethod', multiple='stack', bins=20)
plt.title('Histograma de Cargos Mensuales por Tipo de Pago')
plt.xlabel('Cargos Mensuales')
plt.ylabel('Frecuencia')
plt.legend(title='Tipo de Pago')
plt.show()

# Diagrama de dispersión entre Cargos Mensuales y Cargos Totales por Tipo de Pago
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_contratos, x='MonthlyCharges', y='TotalCharges', hue='PaymentMethod', alpha=0.7)
plt.title('Diagrama de Dispersión de Cargos por Tipo de Pago')
plt.xlabel('Cargos Mensuales')
plt.ylabel('Cargos Totales')
plt.legend(title='Tipo de Pago')
plt.show()

# Matriz de correlación y mapa de calor con variables numéricas y codificación de tipo de pago
df_encoded = pd.get_dummies(df_contratos, columns=['PaymentMethod'])
correlation_matrix = df_encoded.corr()
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Matriz de Correlación con Codificación de Tipo de Pago')
plt.show()

# %% [markdown]
# <div class="alert alert-block alert-danger">
#     <b>Comentarios del Revisor</b> <a class="tocSkip"></a><br>
# excelente desarrollo e intuición de las gráficas, pero es necesario corregir las variables del eje y para la correcta visualización.</div>

# %% [markdown]
# <div class="alert alert-block alert-danger">
#     <b>Comentarios del Revisor</b> <a class="tocSkip"></a><br>
# En este punto, antes de seguir adelante, te recomendaría realizar un análisis visual breve. Esto te ayudará a tener una idea clara de cómo lucen los datos. Podrás extraer conclusiones sobre cómo están distribuidos, si hay valores inusuales y también identificar posibles correlaciones.
#     
# - intenta obtener histogramas, más diagramas de dispersión, correlaciones. No con el objetivo de describir a nivel negocio. Más bien obtener la forma de tus datos.    
#     
# 
# Además, esto te brindará información valiosa sobre el equilibrio entre las diferentes clases de datos. Estas exploraciones serán realmente útiles para afinar tu plan de trabajo. Por ejemplo, podrías definir perfiles más precisos para los candidatos en la sección de modelos. También te darán una indicación sobre si será necesario aplicar técnicas como el bootstrapping o el remuestreo.</div>

# %% [markdown]
# ### Internet
# 

# %%
# Contar la cantidad de cada tipo de servicio de Internet
internet_counts = df_internet["InternetService"].value_counts()
plt.bar(internet_counts.index, internet_counts.values)
plt.title("Distribución de tipos de servicio de Internet")
plt.xlabel("Tipo de servicio de Internet")
plt.ylabel("Número de clientes")
plt.show()

# Lista de características en línea
online_features = ["OnlineSecurity", "OnlineBackup", "DeviceProtection", "TechSupport", "StreamingTV", "StreamingMovies"]

# Iterar a través de las características y crear gráficos apilados
for feature in online_features:
    feature_counts = df_internet.groupby(["InternetService", feature]).size().unstack()
    feature_counts.plot(kind="bar", stacked=True)
    plt.title(f"Distribución de {feature}")
    plt.xlabel("Tipo de servicio de Internet")
    plt.ylabel("Número de clientes")
    plt.legend(title=feature)
    plt.show()


# %% [markdown]
# ### Personal

# %%
# Gráfico de barras para género
gender_counts = df_personal["gender"].value_counts()
plt.bar(gender_counts.index, gender_counts.values)
plt.title("Distribución de género")
plt.xlabel("Género")
plt.ylabel("Número de clientes")
plt.show()

# Gráfico de barras para SeniorCitizen
senior_counts = df_personal["SeniorCitizen"].value_counts()
senior_labels = ["No", "Yes"]
plt.bar(senior_labels, senior_counts)
plt.title("Distribución de SeniorCitizen")
plt.xlabel("SeniorCitizen")
plt.ylabel("Número de clientes")
plt.show()

# Gráfico de barras para Partner
partner_counts = df_personal["Partner"].value_counts()
plt.bar(partner_counts.index, partner_counts.values)
plt.title("Distribución de Partner")
plt.xlabel("Partner")
plt.ylabel("Número de clientes")
plt.show()

# Gráfico de barras para Dependents
dependents_counts = df_personal["Dependents"].value_counts()
plt.bar(dependents_counts.index, dependents_counts.values)
plt.title("Distribución de Dependents")
plt.xlabel("Dependents")
plt.ylabel("Número de clientes")
plt.show()

# %%
# Variables categóricas a considerar
categorical_variables = ["SeniorCitizen", "Partner", "Dependents"]

# Crear gráficos apilados para cada variable en función del género
for variable in categorical_variables:
    stacked_data = df_personal.groupby(['gender', variable]).size().unstack()
    stacked_data.plot(kind='bar', stacked=True)
    plt.title(f"Relación entre género y {variable}")
    plt.xlabel("Género")
    plt.ylabel("Número de clientes")
    plt.legend(title=variable)
    plt.show()

# %% [markdown]
# <div class="alert alert-block alert-success">
#     <b>Comentarios del Revisor</b> <a class="tocSkip"></a><br>
# 
# Excelente trabajo en tu enfoque. Es fundamental que analicemos las relaciones que existen entre las variables, teniendo en cuenta no solo la correlación, sino también cómo estas variables se comportan en términos de su cardinalidad, distribución de datos y valores. Este paso será crucial para una selección más acertada de los modelos que implementaremos. No olvides que la elección cuidadosa de características es apropiada y que algunos modelos son especialmente sensibles a la colinealidad debido a alta correlación entre las variables. ¡Sigue adelante con este enfoque detallado y considerado!   </div>

# %% [markdown]
# ### Phone

# %%
# Contar la cantidad de cada categoría en la variable MultipleLines
multiple_lines_counts = df_phone["MultipleLines"].value_counts()

# Crear un gráfico de barras
plt.bar(multiple_lines_counts.index, multiple_lines_counts.values)
plt.title("Distribución de MultipleLines")
plt.xlabel("MultipleLines")
plt.ylabel("Número de clientes")
plt.show()

# %% [markdown]
# ## 4 Conclusiones Parciales

# %% [markdown]
# - No se observan valores ausentes en ninguno de los DataFrames, pero si los quiero unir para tener un solo DataFrame se van a presentar valores ausentes por la falta de datos.
# - Según los gráficos podemos ver las siguientes cosas:
#     - En los contratos vemos que la mayoria de los clientes son mensuales, les siguen los de dos años de antigüedad y por último los de 1 año. Y no se observan una relación entre los cargos mensuales y los cargos totales.
#     - En los servicios de internet la mayoria prefiere la fibra optica. En seguridad en linea, backup, protección de aparatos y soporte tecnico se observa que los usuarios de la tecnologia DSL eligen estos servicios mucho menos que los de fibra optica. Las personas que no eligen TV y Peliculas por streaming es casi la misma en ambas tecnologias (DSL y Fibra Optica), pero cuando si las contratan se repite el patron observado anteriormente en donde predomina las personas con fibra óptica.
#     - En el DataFrame de los datos personales, no hay una diferencia entre el genero y un compañero de vivienda a la hora de contratar un servicio, pero si se observan una diferencia entre las personas de 3ra edad y si tienen alguna persona a su cargo, en este caso las personas que contratan los servicios son menos.
#     - Las personas con multiples lineas de telefonos son menores a las que si las poseen. 

# %% [markdown]
# ## 5 Recomendaciones

# %% [markdown]
# Algunas recomendaciones por el momento serian las siguientes:
# 
#  - Ofertas y Promociones Especiales: Dado que la mayoría de los clientes eligen contratos mensuales, podría ser beneficioso ofrecer ofertas y promociones especiales para incentivar a los clientes a optar por contratos más largos, como contratos de 1 o 2 años. Esto podría ayudar a mejorar la retención de clientes a largo plazo.
#  
# - Mejora de Servicios DSL: Dado que se observa una preferencia por la fibra óptica y una menor adopción de servicios adicionales entre los usuarios de DSL, podrían considerar mejorar y diversificar tus ofertas de servicios DSL. Esto podría incluir mejoras en la velocidad, así como incentivos para la adopción de servicios de seguridad en línea, copias de seguridad y protección de dispositivos.
# 
# - Segmentación de Clientes: Dado que las personas mayores con dependientes son menos propensas a contratar servicios, podrían considerar una estrategia de segmentación específica para este grupo demográfico. Puedes ofrecer servicios adaptados a sus necesidades y preocupaciones específicas, lo que podría aumentar su interés en la adopción.
# 
# - Mejora de la Oferta de Streaming: La preferencia por la fibra óptica en relación con los servicios de streaming indica una oportunidad para mejorar la calidad y la oferta de contenido en streaming para los usuarios de DSL. Esto podría atraer a más clientes de DSL a aprovechar estos servicios.
# 
# - Promoción de Líneas Múltiples: Dado que las personas con múltiples líneas son menos comunes, podrían considerar promocionar los beneficios de tener múltiples líneas de teléfono en términos de conveniencia y funcionalidad. Esto podría aumentar la adopción de este servicio.
# 

# %% [markdown]
# ## 6 Próximos Pasos

# %% [markdown]
# Crear un solo DataFrame con todos los datos para su mejor manipulacion, convertir las columnas de fechas (como "BeginDate" y "EndDate") a tipos de datos datetime64 en lugar de mantenerlos como objetos lo que permitirá realizar operaciones de manipulación y cálculos de fechas de manera más eficiente y precisa, además de facilitar el análisis.
# 
# <div class="alert alert-block alert-warning">
#     <b>Comentarios del Revisor</b> <a class="tocSkip"></a><br>Es importante establcer con qué métricas evaluaremos los proyectos. Podrías utilizar AUC-ROC como métrica principal es sólida.  También podrías considerar precisión, recall y F1-score, ya que proporcionan una imagen más completa del rendimiento del modelo de acuerdo al balance de clases que observes en tu problema.
# </div>
# 
# Establecer valores de AUC-ROC, precision, recall y F1-score con un dummy para comparar los valores obtenidos si son mejores estos quiere decir que el modelo es bueno si son menores quiere decir que no sirve
# 
# Dado que los datos contienen tanto características categóricas como numéricas, podría ser útil considerar algoritmos que manejen ambas. Por ejemplo, los bosques aleatorios y los algoritmos de boosting como XGBoost o LightGBM suelen funcionar bien en este tipo de conjuntos de datos mixtos.

# %% [markdown]
# <div class="alert alert-block alert-warning">
#     <b>Comentarios del Revisor</b> <a class="tocSkip"></a><br>
# 
# Excelente trabajo en tu enfoque. Sin enmabro es fundamental que  antes de avanzar analicemos las relaciones que existen entre las variables, teniendo en cuenta no solo la correlación, sino también cómo estas variables se comportan en términos de su cardinalidad, distribución de datos y valores. Este paso será crucial para una selección más acertada de los modelos que implementaremos!. 
# 
# Esto es diferente de una exploración de datos EDA como la que has planteado, pues esa sección nos hablará de las observaciones de negocio y como esta se implican en el contexto de los objetivos del análisis. Por ejemplo, ¿cómo podrían los patrones demográficos influir en la adopción de servicios o en la toma de decisiones comerciales?</div>


