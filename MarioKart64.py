#!/usr/bin/python2

import gym, gym_mupen64plus

class MarioKart64:
	def __init__(self, map_name):
		self.env = gym.make(map_name)
		self.state = dict()
		self.visibility = False
		self.action = [0, 0, 0, 0, 0]


	def new_episode(self):
		self.state['observation'] = self.env.reset()
		self.action = [0, 0, 0, 0, 0]
		if self.visibility:
			self.env.render()
		for i in range(88):
			(obs, reward, end, info) = self.env.step(self.action)
			if self.visibility:
				self.env.render()
		self.state['observation'] = obs
		self.state['reward'] = 0
		self.state['end'] = end
		self.state['info'] = info


	def get_state(self):
		return self.state


	def make_action(self, action, frame_repeat):
		action_reward = 0
		for i in range(frame_repeat):
			(obs, reward, end, info) = self.env.step(action)
			action_reward += reward
			if end:
				break
		if self.visibility:
			self.env.render()
		self.state['observation'] = obs
		self.state['reward'] += action_reward
		self.state['end'] = end
		self.state['info'] = info
		return action_reward


	def is_episode_finished(self):
		return self.state['end']


	def get_total_reward(self):
		return self.state['reward']


	def set_window_visible(self, visibility):
		self.visibility = visibility


	def set_action(self, action):
		self.action = action


	def advance_action(self):
		if self.state['end']:
			return 0
		(obs, reward, end, info) = self.env.step(self.action)
		if self.visibility:
			self.env.render()
		self.state['observation'] = obs
		self.state['reward'] += reward
		self.state['end'] = end
		self.state['info'] = info
		return reward


	def get_all_actions(self):
		return self.env.action_space

	def close(self):
		self.env.close()
