import pandas as pd
import numpy as np
import seaborn as sns

train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')
sub = pd.read_csv('gender_submission.csv')
int(1.1)
train.query('Age <10')['Survived'].mean()
fig, ax = plt.subplots(figsize=(10,5),constrained_layout=True)

# sns.kdeplot(x='body_mass_g', data=df, fill=True, ec='gray',fc='white',ax=ax) # fc= fill color, ec= edge color
# sns.kdeplot(x='body_mass_g', data=df, hue='species',fill=True, ax=ax)

sns.kdeplot(data= train, train['Age'], hue=train['Pclass']) 
train['Age'][train['Pclass'] == 1].plot(kind='kde')
sns.kdeplot(x='Age', data=train, hue='Pclass')
sns.kdeplot(x='Age', data=train)

sns.barplot(data=train, x=options[0], y='Survived', hue=options[0], palette=sns.cubehelix_palette(), ci=None, ax=axs[0])
sorted(train['Pclass'].unique())
print(a)
train.info()
sns.heatmap(train.isnull())
len(train)
missing = train.isnull().mean().to_frame().reset_index()
missing = missing.rename(columns={0:'ratio'})
f"{float(missing.query('index=="Embarked"')['ratio'])*100:.2f}%"
f"{float(a.query('index=="Age"')[0])*100:.2f}%"
train.columns
train['Cabin'].value_counts()

train.query('Ticket == "347082"')
train.query('Cabin == "B96 B98"')

train.select_dtypes(include = [object])

tickets = train['Ticket'].value_counts().to_frame().reset_index()
tickets = tickets[tickets['count']>1]
tickets.groupby('count',as_index=False).agg(n=('count','count')).sort_values('count',ascending=False)

cabins = train['Cabin'].value_counts().to_frame().reset_index()
cabins = cabins[cabins['count']>1]
cabins.groupby('count',as_index=False).agg(n=('count','count')).sort_values('count',ascending=False)


corr = train.select_dtypes(include = [int, float]).corr()
corr 
# 히트맵 시각화
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=0.5)
corr["Survived"].sort_values(ascending = True)

sns.pairplot(train)

train.columns
train.groupby('Pclass',as_index=False).agg(survived=lambda x : lambda x['Survived'].mean(), non= lambda x: 1-survived)
sns.barplot(data=train,x='Pclass',y='Survived',hue='Pclass')

result = train.groupby('Pclass', as_index=False).agg(
    survived=('Survived', 'mean'),  # 생존률
    non_survived=('Survived', lambda x: 1 - x.mean())  # 비생존률
)

result

result.set_index('Pclass', inplace=True)
result.plot(kind='bar', stacked=True, figsize=(8, 6))

# 그래프 설정
plt.title('Stacked Bar Plot of Survival by Pclass')
plt.xlabel('Pclass')
plt.ylabel('Proportion')
plt.xticks(rotation=0)
plt.legend(title='Survival Status', labels=['Not Survived', 'Survived'])
plt.show()

train.columns
palette = {0: '#A9A9A9', 1: '#4A90E2'} 
# 클래스 별 생존률

sv = train.groupby('Pclass', as_index=False)['Survived'].sum()
sv['ratio'] = sv['Survived']/ len(train)
pd.crosstab(train['Pclass'], train['Survived'], margins=True)
sns.barplot(data=train,x='Pclass',y='Survived',hue='Pclass', ci=None)
sns.countplot(data=train,x='Pclass',hue='Survived', palette=palette)

train.groupby(['Sex'])['Survived'].mean()

sns.barplot(data=train,x='Sex',y='Survived',hue='Sex', ci=None)
sns.countplot(data=train,x='Sex',hue='Survived', palette=palette)

plt.xticks([1, 2, 3]) 
sns.lineplot(data=train, x="Pclass", y="Survived", hue="Sex", marker='o', ci=None)


with st.container():
    st.subheader('2️⃣ 변수들간의 관계 확인하기')
    with st.expander("코드보기"):
        st.code('''
    # 변수들 간 산포도 시각화 
    sns.pairplot(train)
                
    # 상관계수 시각화
    # corr = train.select_dtypes(include = [int, float]).corr()
    # fig, ax = plt.subplots()
    # sns.heatmap(ax=ax, data=corr, annot=True, cmap='coolwarm', linewidths=0.5)
                ''')
    col1, col2 = st.columns([2,1])
    sns.pairplot(train)
    col1.pyplot(plt.gcf())
    col2.warning('**선형의 상관관계가 보이지 않는다**', icon="🤔")



    # Sex
    plt.rcParams['font.family'] ='Malgun Gothic'
    fig, axs = plt.subplots(1, 2, figsize=(12, 4))
    
    sns.barplot(data=train, x='Sex', y='Survived', hue='Sex', palette=sns.cubehelix_palette(), ci=None, ax=axs[0])
    axs[0].set_title('Sex 내 Survived비율')

    sns.countplot(data=train, x='Sex', hue='Survived', palette=mypalette, ax=axs[1])
    axs[1].set_title('Sex 내 Survived 수')

    st.pyplot(plt.gcf())
    st.info('**Pclass**')
    
    # Pclass & Sex
    plt.rcParams['font.family'] ='Malgun Gothic'  
    
    fig, ax = plt.subplots()
    sns.lineplot(ax=ax, data=train, x="Pclass", y="Survived", hue="Sex", marker='o', ci=None)
    ax.set_xticks([1, 2, 3])
    st.pyplot(fig)
    st.info('**Pclass**')
    
mypalette = {0: '#A9A9A9', 1: '#4A90E2'} 
counts= train.groupby(['Pclass','Sex','Survived']).agg(n=('Survived','count'))
counts
sns.countplot(data=counts, x='Pclass', hue='Survived', palette=mypalette)

train.groupby('Pclass')['Survived'].mean()