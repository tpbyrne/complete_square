from manim import *

TITLE_1 = "Completing the Square"
TITLE_2 = "Solve the Quadratic"
TITLE_3 = "Solve by Inspection"
TITLE_4 = "Geometric Interpretation"
TITLE_5 = "Complete the Square"
TITLE_6 = "Rectangle as Difference of Two Squares"
TITLE_7 = "Solving the Equation"
TITLE_8 = "Checking Results with..."

class Opening(Scene):
    def construct(self):
        title = Title(f" {TITLE_1}")
        self.add(title)
        banner = ManimBanner()
        self.play(banner.create())
        self.play(banner.expand())
        self.wait()
        self.play(Unwrite(banner))
        self.remove(title)
        self.wait()

class ProblemStatement(Scene):
    def construct(self):

        title = Title(f" {TITLE_2}")
        self.add(title)
        eq1 = MathTex(r"x^2 + 3x -1 = 0")

        self.play(Write(eq1))
        self.wait(18)
        self.play(Unwrite(eq1))
        self.remove(title)

class SolveByInspection(Scene):
    def construct(self):

        title = Title(f" {TITLE_3}")
        self.add(title)
        eq1 = MathTex(r"x^2", r"+ 3x", r" -1", r" = 0").shift(2*UP)

        eq2 = MathTex(r"{{( x + \alpha ) }}",          r"{{( x + \beta ) }}",          "",                      "=", "{{0}}")
        eq3 = MathTex(r"{{x^2 }}",                     r"{{+{\alpha}{x}+{\beta}{x}}}", r"{{+{\alpha}{\beta}}}", "=", "{{0}}")
        eq4 = MathTex(r"{{x^2 }}",                     r"{{+x({\alpha}+{\beta})}}",    r"{{+{\alpha}{\beta}}}", "=", "{{0}}")

        eq5 = MathTex(r"({\alpha} + {\beta}) & = 3  ", r"\\ {\alpha}{\beta} & = -1 ")

        self.add(eq1)
        self.add(eq2)

        self.wait(2.5)
        self.play(TransformMatchingTex(eq2, eq3, path_arc=PI/2))
        self.wait(4.5)

        self.play(TransformMatchingTex(eq3, eq4, path_arc=PI/2))
        self.wait(2.5)
        self.play(eq1[1].animate.set_color(YELLOW))
        self.play(eq4[1].animate.set_color(YELLOW))
        
        self.play(eq1[2].animate.set_color(RED))
        self.play(eq4[2].animate.set_color(RED))

        self.wait(2.5)
        self.play(TransformMatchingTex(eq4, eq5, path_arc=PI/2))
        self.wait(2.5)

        self.play(eq5[0].animate.set_color(YELLOW))
        
        self.play(eq5[1].animate.set_color(RED))
        self.wait(16)

        self.remove(eq5)
        self.remove(title) 

class GeometricInterpretation(Scene):
    def construct(self):

        title = Title(f" {TITLE_4}")
        self.add(title)

        eq1_a   = MathTex("{{x}}^2", "{{+}}", "{{3}}", "{{x}}")
        eq1_b   = MathTex( r"-2 = 0").next_to(eq1_a, direction=RIGHT)
        eq2     = MathTex("{{x}}^2", "{{+}}", "{{b}}", "{{x}}")
        eq3     = MathTex("{{x}}",   "{{(x}}", "{{+}}", "{{b)}}")

        self.add(eq1_a, eq1_b)
        self.wait()
        self.play(ShrinkToCenter(eq1_b))
        self.wait()

        self.wait(2.5)
        self.play(TransformMatchingTex(eq1_a, eq2, path_arc=PI/2))
        self.wait(2.5)
        self.play(TransformMatchingTex(eq2, eq3, path_arc=PI/2))
    
        self.add(eq3)
        self.wait(4)

        r1 = Rectangle(color=YELLOW, height=4,width=3)

        br_x =  always_redraw( lambda: Brace(r1))
        br_y =  always_redraw( lambda: Brace(r1, direction=LEFT))
        t_y  =  always_redraw( lambda: br_y.get_tex(r"x + b"))
        t_x  =  always_redraw( lambda: br_x.get_tex(r"x"))

        a =  always_redraw( lambda:  MathTex(r"area = \\ x^2+bx").move_to(r1.get_center()))

        x = VGroup(r1).arrange(direction=DOWN,buff=0)
        x.add(br_x, br_y, t_x, t_y, a)

        self.play(Transform(eq3, x.to_edge(LEFT+DOWN)))
        self.wait(4)

        self.wait(5)
       
        self.clear()

        text = Text("Alternatively...")
        self.play(Write(text))
        self.wait()
        self.play(Unwrite(text))

        eq3 = MathTex(r"x^2", r"+ bx")

        self.add(eq3)
        self.wait(3)

        s1 = Square(color=YELLOW, side_length=3)
        
        br_x = always_redraw( lambda: Brace(s1))
        br_y = always_redraw( lambda: Brace(s1, direction=LEFT))
        t_y  = always_redraw( lambda: br_y.get_tex(r"x"))
        t_x  = always_redraw( lambda: br_x.get_tex(r"x"))

        a = always_redraw( lambda: MathTex(r"area = x^2").move_to(s1.get_center()))

        x = VGroup(s1)
        x.add(br_x, br_y, t_x, t_y, a)

        r0 = Rectangle(color=YELLOW, height=1,width=3)

        # To get the shapes to align within the VGroup we use the buff value below
        br_r0_y = Brace(r0, direction=LEFT, buff=0.27)
        t_r0_y  = br_r0_y.get_tex(r"b")
        a_r0    = MathTex(r"area = bx").move_to(r0.get_center())

        y = VGroup(r0)
        y.add( br_r0_y, t_r0_y, a_r0)

        self.play(Transform(eq3[0], x.to_edge(LEFT+DOWN)))
        self.wait(4)

        self.play(Transform(eq3[1], y.next_to(x, direction=UP, buff=0)))
        self.wait(16)

        self.remove(title)

        self.clear()

class CompleteTheSquare(Scene):
    def construct(self):

        title = Title(f" {TITLE_5}")
        self.add(title)

        r0 = Rectangle(color=YELLOW, height=4,width=3).shift(0.5*DOWN)

        br_r0_x = Brace(r0)
        br_r0_y = Brace(r0, direction=LEFT)
        t_r0_y = br_r0_y.get_tex(r"x + b")
        t_r0_x = br_r0_x.get_tex(r"x")

        self.add(r0,br_r0_x,br_r0_y,t_r0_y,t_r0_x)

        self.wait(4)

        s1 = Square(color=YELLOW, side_length=3).shift(1*DOWN)
        br_x = always_redraw( lambda: Brace(s1))
        br_y = always_redraw( lambda: Brace(s1, direction=LEFT))
        t_y =  always_redraw( lambda:br_y.get_tex(r"x"))
        t_x =  always_redraw( lambda:br_x.get_tex(r"x"))

        r1 = Rectangle(color=YELLOW, height=0.5, width=3).shift(1*UP)
        br_r1_y = always_redraw( lambda: Brace(r1, direction=LEFT))
        t_r1_y = always_redraw( lambda: br_r1_y.get_tex(r"b/2")) 

        r2 = Rectangle(color=YELLOW, height=0.5, width=3).shift(2*UP)
        br_r2_y = always_redraw( lambda: Brace(r2, direction=LEFT))
        t_r2_y = always_redraw( lambda: br_r2_y.get_tex(r"b/2")) 

        self.remove(r0, br_r0_x,br_r0_y,t_r0_y,t_r0_x)

        self.add(s1, r1, r2, br_x, br_y, t_x, t_y, br_r1_y, t_r1_y, br_r2_y, t_r2_y  )
        
        self.wait()
        self.play(r1.animate.next_to(s1, UP, buff=0))
        self.play(r2.animate.next_to(r1, UP, buff=0))

        self.remove(br_r2_y, t_r2_y )
        self.wait()

        self.play(
            r2.animate.shift(2*DOWN + 3*RIGHT)
        )
        self.play(r2.animate.rotate(PI/2))

        self.wait()

        self.play(r2.animate.next_to(s1, RIGHT, buff=0))

        self.wait()

        br_r2_x = always_redraw( lambda: Brace(r2, direction=DOWN))
        t_r2_x = always_redraw( lambda: br_r2_x.get_tex(r"b/2")) 

        self.add(br_r2_x, t_r2_x)

        s2 = Square(side_length=0.5, color=BLUE,fill_opacity=1).next_to(r1, RIGHT, buff=0)
        
        self.wait(4)

        self.add(s2)

        self.wait(3)
        
        self.remove(s2, br_r2_x, t_r2_x ,s1, r1, r2, br_x, br_y, t_x, t_y, br_r1_y, t_r1_y, br_r2_y, t_r2_y )

        s4 = Square(side_length=3.5, color=RED).shift(0.75*DOWN+0.25*RIGHT)
        br_x = always_redraw( lambda: Brace(s4))
        br_y = always_redraw( lambda: Brace(s4, direction=LEFT))
        t_y =  always_redraw( lambda:br_y.get_tex(r"x + b/2"))
        t_x =  always_redraw( lambda:br_x.get_tex(r"x + b/2"))

        self.add(s4, br_x, br_y, t_x, t_y )

        self.wait(4)        
        
        s5 = Square(side_length=0.5, color=BLUE,fill_opacity=1).next_to(s4, RIGHT+UP, buff=0).shift(0.5*LEFT+0.5*DOWN)
        br_s5_x = always_redraw( lambda: Brace(s5, direction=UP))
        br_s5_y = always_redraw( lambda: Brace(s5, direction=RIGHT))
        t_s5_y =  always_redraw( lambda:br_s5_y.get_tex(r"b/2"))
        t_s5_x =  always_redraw( lambda:br_s5_x.get_tex(r"b/2"))
        self.add(s5)
        self.add(br_s5_x, br_s5_y, t_s5_y, t_s5_x)
        self.wait(16)
        self.remove(title)

        self.clear()

class DifferenceOfTwoSquares(Scene):
    def construct(self):
        
        title = Title(f" {TITLE_6}")
        self.add(title)



        eqn_1 = MathTex(r"{{(x + b/2)^2}}",  r"{{=}}", r"{{x(x + b)}}",    r"{{+}}", r"{{ (b/2)^2}}")
        eqn_2 = MathTex(r"{{(x + b/2)^2}}",  r"{{-}}", r"{{ (b/2)^2}}",    r"{{=}}", r"{{x(x + b)}}")
        eqn_3 = MathTex(r"{{x(x + b)}}",     r"=",     r"{{(x + b/2)^2}}", r"{{-}}", r"{{ (b/2)^2}}")

        eqn_1[0].set_color(RED)
        eqn_1[2].set_color(YELLOW)
        eqn_1[4].set_color(BLUE)

        eqn_2[0].set_color(RED)
        eqn_2[2].set_color(BLUE)
        eqn_2[4].set_color(YELLOW)

        eqn_3[0].set_color(YELLOW)
        eqn_3[2].set_color(RED)
        eqn_3[4].set_color(BLUE)

        self.add(eqn_1)
        self.wait(5.5)
        self.play(TransformMatchingTex(eqn_1, eqn_2, path_arc=PI/2))
        self.wait(5.5)
        self.play(TransformMatchingTex(eqn_2, eqn_3, path_arc=PI/2))      
        self.wait(5.5)
        self.play(eqn_3.animate.shift(3*DOWN))

        r0 = Rectangle(color=YELLOW, height=4,width=3)
        equals = Text("equals")
        minus = Text("minus")
        s4 = Square(side_length=3.5, color=RED)
        s5 = Square(side_length=0.5, color=BLUE,fill_opacity=1)


        self.wait()

      
        self.play(Transform(eqn_3[0], r0.shift(5*LEFT)))
        self.wait()
        self.play(Transform(eqn_3[1], equals.shift(2*LEFT)))
        self.wait()
        self.play(Transform(eqn_3[2], s4.shift(1*RIGHT)))
        self.wait()
        self.play(Transform(eqn_3[3], minus.shift(4*RIGHT)))
        self.wait()
        self.play(Transform(eqn_3[4], s5.shift(5.5*RIGHT)))
        
        eqn = MathTex(r"x(x + b)", r"=", r"(x + b/2)^2", r" -", r" (b/2)^2").shift(3*DOWN)
        eqn[0].set_color(YELLOW)
        eqn[2].set_color(RED)
        eqn[4].set_color(BLUE)

        self.wait(6)
        self.play(Write(eqn))
       
        self.wait(16)

        self.clear()

class Solving(Scene):
    def construct(self):
        
        title = Title(f" {TITLE_7}")
        self.add(title)

        eq1 = MathTex("{{x}}^2",          "{{+}}",  "{{3}}",       "{{x}}",       "{{-}}", "{{1}}",       "{{=}}",           "{{0}}")
        eq2 = MathTex("{{x(}}",           "{{x}}",  "{{+}}",       "{{3)}}",      "{{-}}", "{{1}}",       "{{=}}",           "{{0}}")

        eq3 = MathTex("{{(x + 3/2)}}^2",  "{{-}}",  "{{(3/2)}}^2", "{{-}}",       "{{1}}", "{{}}",        "{{=}}",           "{{0}}")
        eq4 = MathTex("{{(x + 3/2)}}^2",  "{{}}",   "{{}}",        "{{}}",        "{{=}}", "{{(3/2)}}^2", "{{+}}",           "{{1}}")
        eq5 = MathTex("{{(x + 3/2)}}^2",  "{{}}",   "{{}}",        "{{}}",        "{{}}",  "{{}}",        "{{=}}",           "{{\dfrac{(9 + 4)}{4}}}")
        eq6 = MathTex("{{(x + 3/2)}}^2",  "{{}}",   "{{}}",        "{{}}",        "{{}}",  "{{}}",        "{{=}}",           "{{13/4}}")
        eq7 = MathTex("{{x}}",            "{{+}}",  "{{3}}",       "{{/}}",       "{{2}}", "{{=}}",       "{{}}",        r"{{\pm \dfrac{\sqrt{13} }{2} }}")
        eq8 = MathTex("{{x}}",            "{{}}",   "{{=}}",       "{{}}",        "{{}}",  "{{}}",        r"{{ \dfrac{-3 \pm \sqrt{13} }{2} }}",  "{{}}")

        self.add(eq1)
        self.wait(3.5)
        self.play(TransformMatchingTex(eq1, eq2, path_arc=PI/2))
        self.wait(3.5)

        self.play(TransformMatchingTex(eq2, eq3, path_arc=PI/2))
        self.wait(3.5)

        self.play(TransformMatchingTex(eq3, eq4, path_arc=PI/2))
        self.wait(2.5)

        self.play(TransformMatchingTex(eq4, eq5, path_arc=PI/2))
        self.wait(2.5)

        self.play(TransformMatchingTex(eq5, eq6, path_arc=PI/2))
        self.wait(2.5)
    
        self.play(TransformMatchingTex(eq6, eq7, path_arc=PI/2))
        self.wait(2.5)

        self.play(TransformMatchingTex(eq7, eq8, path_arc=PI/2))
        self.wait(16)
   
        self.clear()

class Checking(Scene):
    def construct(self):
        
        title = Title(f" {TITLE_8}")
        self.add(title)

        text = MathTex(r"{{ x = \dfrac{-3 + \sqrt{13} }{2} }}")
        self.play(Write(text))
        self.wait()
        self.play(text.animate.move_to(1.5*UP+3*LEFT))
        self.play(text.animate.scale(0.6))

        eq10 = MathTex("{{ \left[ \dfrac{-3 + \sqrt{13} } {2} \r] ^2 }}",  "{{+ \dfrac{ 3(-3 + \sqrt{13}) }{2} }}",  "{{-1}}", "=", "{{0}}")
        eq11 = MathTex("{{ \dfrac{9 - 6\sqrt{13} + 13 }{4} }}",            "{{+ \dfrac{-9 + 3\sqrt{13} }{2} }}",     "{{-1}}", "=", "{{0}}")
        eq12 = MathTex("{{ \dfrac{22 - 6\sqrt{13} }{4} }}",                "{{+ \dfrac{-18 + 6\sqrt{13} }{4} }}",    "{{-1}}", "=", "{{0}}")
        eq13 = MathTex("{{ \dfrac{4}{4} }}",                               "{{}}",                                   "{{-1}}", "=", "{{0}}")

        self.play(Create(eq10))
        self.wait(2.5)
        self.play(TransformMatchingTex(eq10, eq11, path_arc=PI/2))
        self.wait(2.5)
        self.play(TransformMatchingTex(eq11, eq12, path_arc=PI/2))
        self.wait(2.5)
        self.play(TransformMatchingTex(eq12, eq13, path_arc=PI/2))
        
        self.play(text.animate.set_color(PURE_GREEN))

        self.wait(5.5)        
        self.clear()

        plane = NumberPlane((-14, 14), (-8, 8))

        function = lambda x: (x**2 + 3*x -1)
        graph = plane.plot(function, color=PURE_RED)

        from math import sqrt

        root_1 = Dot([(-3 + sqrt(13))*0.5, 0, 0])
        root_2 = Dot([(-3 - sqrt(13))*0.5, 0, 0])
        root_1_text = MathTex(r"{{ x = \dfrac{-3 + \sqrt{13} }{2} }}").next_to(root_1, UP + RIGHT)
        root_2_text = MathTex(r"{{ x = \dfrac{-3 - \sqrt{13} }{2} }}").next_to(root_2, 0.6*DOWN + LEFT)
        eq1 = MathTex(r"x^2 + 3x -1 = 0").shift(2.5*UP+2*LEFT)

        self.play(Create(plane))
        self.play(Create(graph))
        self.play(Create(eq1))
        self.play(Create(root_1))
        self.play(Create(root_1_text))       
        self.play(Create(root_2))
        self.play(Create(root_2_text))
        self.wait(16)

        
