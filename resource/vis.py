import geopandas as gpd
import pandas as pd
import folium
from shapely.geometry import Polygon

# CSV 파일 경로
csv_file = '동대문구보행노인사고다발.csv'

# CSV 파일 불러오기
data = pd.read_csv(csv_file, header=0)
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

# 지도 출력
m
