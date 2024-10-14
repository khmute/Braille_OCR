import json


def calc_avg_size(boxes_by_lines):
    total_boxes = 0
    total_size_x = 0
    total_size_y = 0
    total_gap = 0
    
    for line in boxes_by_lines:
        for i, box in enumerate(line):
            if i != 0:
                total_boxes += 1
                total_size_x += box[2] - box[0]
                total_size_y += box[3] - box[1]
                total_gap += box[0] - line[i-1][2]
                
    return total_size_x / total_boxes, total_size_y / total_boxes, total_gap / total_boxes


def make_box(avg_box_size_x, avg_box_size_y, avg_gap, prev_box_right, prev_box_top):
    new_x1 = prev_box_right + avg_gap
    new_x2 = new_x1 + avg_box_size_x
    new_y1 = prev_box_top
    new_y2 = new_y1 + avg_box_size_y
    new_box = [new_x1, new_y1, new_x2, new_y2]
    return new_box
    

def make_boxes(pred_boxes_by_lines):
    avg_box_size_x, avg_box_size_y, avg_gap = calc_avg_size(pred_boxes_by_lines)
    
    for i, line in enumerate(pred_boxes_by_lines):
        for j, box in enumerate(line):
            if j == 0:
                continue
            if box == 0:
                prev_box_right = line[j-1][2]
                prev_box_top = line[j-1][1]
                new_box = make_box(avg_box_size_x, avg_box_size_y, avg_gap, prev_box_right, prev_box_top)
                line[j] = new_box
        pred_boxes_by_lines[i] = line
    
    return pred_boxes_by_lines

        
def levenshtein_distance_with_path(str1, str2):
    len1, len2 = len(str1), len(str2)
    
    # 초기화: 2차원 DP 테이블 및 경로 테이블 생성
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
    path = [[[] for _ in range(len2 + 1)] for _ in range(len1 + 1)]
    
    # 첫 번째 문자열에 대한 초기값 설정 (삽입 작업)
    for i in range(1, len1 + 1):
        dp[i][0] = i
        path[i][0] = path[i-1][0] + [f"Delete '{str1[i-1]}' at position {i-1}"]
    
    # 두 번째 문자열에 대한 초기값 설정 (삽입 작업)
    for j in range(1, len2 + 1):
        dp[0][j] = j
        path[0][j] = path[0][j-1] + [f"Insert '{str2[j-1]}' at position {j-1}"]
    
    # DP 테이블 및 경로 테이블 채우기
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # 문자가 같으면 비용 없이 대체
                path[i][j] = path[i - 1][j - 1]  # 경로 유지
            else:
                # 삭제, 삽입, 대체 중 최소 비용 선택
                delete_cost = dp[i - 1][j] + 1
                insert_cost = dp[i][j - 1] + 1
                replace_cost = dp[i - 1][j - 1] + 1
                
                min_cost = min(delete_cost, insert_cost, replace_cost)
                dp[i][j] = min_cost
                
                # 경로 추적
                if min_cost == delete_cost:
                    path[i][j] = path[i - 1][j] + [f"Delete '{str1[i-1]}' at position {i-1}"]
                elif min_cost == insert_cost:
                    path[i][j] = path[i][j - 1] + [f"Insert '{str2[j-1]}' at position {j-1}"]
                else:
                    path[i][j] = path[i - 1][j - 1] + [f"Replace '{str1[i-1]}' with '{str2[j-1]}' at position {i-1}"]

    return dp[len1][len2], path[len1][len2]


def feedback_gen(extracted_json):
    pred_boxes_by_lines = extracted_json['prediction']['boxes_by_lines']
    make_boxes(pred_boxes_by_lines)
    
    pred_brls = extracted_json['prediction']['brl']
    corr_brls = extracted_json['correction']['brl']
    
    for pred_brl, corr_brl in zip(pred_brls, corr_brls):
        distance, operations = levenshtein_distance_with_path(pred_brl, corr_brl)
        
        print(f"예측: {pred_brl}")
        print(f"수정: {corr_brl}")
        print(f"레벤슈타인 거리: {distance}")
        print("변환 경로:")
        for step in operations:
            print(step)
        print()
    

if __name__ == "__main__":
    extracted_json = {
        "prediction": {
            "brl": [
                "⠔⠔⠶⠨⠐⠍  ⠰⠈⠠⠥⠗⠣⠡⠤⠝⠢⠵⠐  ⠕  ⠠⠏⠨⠾⠕  ⠔⠶⠨⠎⠺"
            ]
        },
        "correction": {
            "brl": [
                "⠔⠶⠨⠐⠍ ⠰⠈⠠⠥⠗⠣⠡⠤⠝⠢⠵⠐ ⠕ ⠠⠏⠨⠾⠕ ⠔⠶⠨⠎⠺"
            ]
        }
    }
    
    feedback_gen(extracted_json)