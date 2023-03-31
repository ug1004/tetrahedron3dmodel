import pygame
from pygame.locals import*
from OpenGL.GL import*
from OpenGL.GLU import*

def my_find_center_position(t_a, t_b, t_c):
    '''이 함수는 세개의 3차원 좌표를 받아서 중심점 좌표를 반환합니다.
       독스트링 여러 줄로 ...'''
    
    t_result = [0, 0, 0]
    for i in range(0,3,1):
        t_result[i] = (t_a[i] + t_b[i] + t_c[i])/3
    return t_result

def my_3DFileLoader(t_filepath):
    with open(t_filepath, 'r', encoding='utf8') as t_file:   # 파일을 읽어서 t_buf1에 저장
        t_buf1 = t_file.readlines()

    t_vex_list = []    # 점좌표 데이터 저장공간
    t_face_list = []   # 면정보 데이터 저장공간

    for x in t_buf1:
        a = x.strip()                                # '\n' 과 같이 숨은 문자열 제거
        a = a.replace(',','')                        # ',' 기호 제거 
        a = a.split(' ')                             # 공백을 기준으로 문자열을 조각내고 리스트로 저장
        

        if a[0] =='v':
            b = [float(a[1]), float(a[2]), float(a[3])]  # 두번째, 세번째, 네번째 문자숫자를 숫자로 변환후 리스트로 저장
            t_vex_list.append(b)                         # 점데이터 3차원 벡터 리스트를 my_vex 리스트에 요소로 넣기

        elif a[0] == 'f':
            b = [int(a[1]), int(a[2]), int(a[3])]  # 두번째, 세번째, 네번째 문자숫자를 숫자로 변환후 리스트로 저장
            t_face_list.append(b)                        # 면정보 3차원 벡터 리스트를 my_face 리스트에 요소로 넣기

    return t_vex_list, t_face_list




def main(t_v, t_f):
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    
    gluPerspective(45, (display[0]/display[1]),0.1, 50.0)
    
    glTranslatef(0.0, 0.0, -5.0)
    
    
    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                
        glRotatef(1,3,1,1)
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        my_draw(t_v, t_f)
        pygame.display.flip()
        pygame.time.wait(10)
        
def my_draw(a_v, a_f):
    glBegin(GL_LINES)
    for f in a_f:
        for i in range(0,3,1):
            glVertex3fv(a_v[f[i  ]])
            if i !=2:
                 glVertex3fv(a_v[f[i+1]])
            else:
                glVertex3fv(a_v[f[0]])
    glEnd()
    

my_vex, my_face = my_3DFileLoader('tetrahedron.txt')
main(my_vex, my_face)
