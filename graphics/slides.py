from manimlib.imports import *


class TheoreticComputerScience(Scene):

	CONFIG = {"camera_config" : {"background_color" : "#fdf6e3" } }
	Mobject.CONFIG['color'] = "#657b83"

	def construct(self):

		np_circle = Circle(radius=3.0, color=BLUE)
		p_circle = Circle(radius=2.0, color=BLUE)
		p = TextMobject("P", color=BLUE)
		np = TextMobject("NP", color=BLUE)
		np.shift(2.7*UP)


		self.play(ShowCreation(p_circle), ShowCreation(p), runtime=2)

		self.play(ShowCreation(np_circle), ShowCreation(np), runtime=2)

		left_equal = TextMobject("P = ", color=BLUE)
		right_equal =TextMobject("NP", color=BLUE)

		left_equal.shift(3.3 * UP)
		left_equal.shift(0.3 * LEFT)
		right_equal.shift(3.3 * UP)
		right_equal.shift(0.7 * RIGHT)

		self.play(Transform(p_circle, np_circle), Transform(p, left_equal), Transform(np, right_equal), runtime = 2)



class RecommenderSystem(Scene):

	CONFIG = {"camera_config" : {"background_color" : "#fdf6e3" } }
	Mobject.CONFIG['color'] = "#657b83"

	def construct(self):

		
		image1 = ImageMobject("media/titanic.jpg").set_height(1)
		image1.move_to(4*RIGHT + 2*UP)

		image2 = ImageMobject("media/wolfofwallstreet.jpg").set_height(1)
		image2.move_to(4*RIGHT)

		image3 = ImageMobject("media/goodfellas.jpg").set_height(1)
		image3.move_to(4*RIGHT + 2 * DOWN)

		bob = ImageMobject("media/bob.png").set_height(1)
		bob.move_to(4 * LEFT + 2 * DOWN)

		alice = ImageMobject("media/alice.png").set_height(1)
		alice.move_to(4*LEFT + 2*UP)


		self.play(ShowCreation(image1), ShowCreation(image2), ShowCreation(image3), ShowCreation(bob), ShowCreation(alice))

		
		arrow = Arrow(4 * LEFT +  2*UP, 4 * RIGHT + 2 * UP, color=RED)
		arrow2 = Arrow(4 * LEFT +  2*UP, 4 * RIGHT, color=GREEN)
		arrow3 = Arrow(4 * LEFT + 2*UP, 4 * RIGHT + 2 *DOWN, color = GREEN)

		arrow4 = Arrow(4*LEFT + 2*DOWN, 4 * RIGHT + 2*UP, color = RED)
		arrow5 = Arrow(4 * LEFT +  2*DOWN, 4 * RIGHT, color=GREEN)
		arrow6 = DashedLine(4 * LEFT + 2*DOWN, 4 * RIGHT + 2*DOWN, color = GREEN).add_tip()

		
		self.play(ShowCreation(arrow), run_time = 2)
		self.play(ShowCreation(arrow2), run_time = 2)
		self.play(ShowCreation(arrow3), run_time = 2)
		self.play(ShowCreation(arrow4), run_time = 2)
		self.play(ShowCreation(arrow5), run_time = 2)
		self.play(ShowCreation(arrow6), run_time = 2)
		
		

		
		

