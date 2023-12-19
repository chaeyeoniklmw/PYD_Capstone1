import geopandas as gpd
import pandas as pd
import folium
from shapely.geometry import Polygon, Point

# CSV 파일 경로
csv_file = '/content/동대문구보행노인사고다발.csv'

# CSV 파일 불러오기
data = pd.read_csv(csv_file, header=0)

# 동대문구의 GeoDataFrame
dongdaemun_gdf = geo_data[geo_data['sggnm'] == '동대문구']

# Folium 지도 생성
m = folium.Map(location=[37.5731056, 127.0590049], zoom_start=15)  # 맵의 중심 설정

# 스타일 함수 정의 (폴리곤 색상 설정)
def style_function(feature):
    return {
        'fillColor': 'red',  # 폴리곤의 색상을 여기서 지정
        'color': 'blue',
        'weight': 0.7,
        'fillOpacity': 0.1,
    }

# 0부터 94까지 다발지역폴리곤을 시각화
for i in range(0, 94):
    polygon_string = data['다발지역폴리곤'].iloc[i]  # 해당 인덱스의 다발지역폴리곤 값 가져오기
    polygon_coords = eval(polygon_string)['coordinates'][0]  # 좌표 추출

    # 폴리곤 생성
    polygon_geom = Polygon(polygon_coords)
    crs = {'init': 'epsg:4326'}  # 좌표계 설정
    polygon_gdf = gpd.GeoDataFrame(index=[0], crs=crs, geometry=[polygon_geom])

    folium.GeoJson(
        polygon_gdf,
        style_function=style_function  # 스타일 함수 적용
    ).add_to(m)  # 폴리곤을 Folium 지도에 추가

# 데이터를 Pandas DataFrame으로 변환
marker_data = {
    '대상시설명': ['동대문노인종합복지관', '중산경노당', '행복마을경노당', '사)대한노인회', '장평경노당', '경동요양병원', '은천노인종합복지센터', '시립동대문실버케어센터'],
    '위도': [37.58723704, 37.57035699, 37.59000925, 37.57637482, 37.57325201, 37.58294153, 37.570683, 37.575637],
    '경도': [127.0500258, 127.0576174, 127.0387016, 127.0563417, 127.0684601, 127.0437706, 127.0722082, 127.044825]
}

marker_df = pd.DataFrame(marker_data)

# DataFrame의 각 행을 반복하여 마커 추가
for index, row in marker_df.iterrows():
    folium.Marker([row['위도'], row['경도']], popup=row['대상시설명']).add_to(m)

# 동대문구 경계 GeoJson 추가
for idx, row in dongdaemun_gdf.iterrows():
    folium.GeoJson(row['geometry'], style_function=lambda x: {'fillColor': 'transparent', 'color': 'black', 'weight': 1.5, 'fillOpacity': 0.5}).add_to(m)


# 지도 출력
m