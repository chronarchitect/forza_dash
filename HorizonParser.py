import imp
from struct import unpack

# Sled / Default format (FM7)
default_format = '<iI27f4i20f5i'

# Dash format (FM7)
dash_format = default_format + '17fH6B3b'

# Horizon format (FH4+)
horizon_format = default_format + 'i19fH6B4b'

params = ['IsRaceOn',
 'TimestampMS',
 'EngineMaxRpm',
 'EngineIdleRpm',
 'CurrentEngineRpm',
 'AccelerationX',
 'AccelerationY',
 'AccelerationZ',
 'VelocityX',
 'VelocityY',
 'VelocityZ',
 'AngularVelocityX',
 'AngularVelocityY',
 'AngularVelocityZ',
 'Yaw',
 'Pitch',
 'Roll',
 'NormalizedSuspensionTravelFrontLeft',
 'NormalizedSuspensionTravelFrontRight',
 'NormalizedSuspensionTravelRearLeft',
 'NormalizedSuspensionTravelRearRight',
 'TireSlipRatioFrontLeft',
 'TireSlipRatioFrontRight',
 'TireSlipRatioRearLeft',
 'TireSlipRatioRearRight',
 'WheelRotationSpeedFrontLeft',
 'WheelRotationSpeedFrontRight',
 'WheelRotationSpeedRearLeft',
 'WheelRotationSpeedRearRight',
 'WheelOnRumbleStripFrontLeft',
 'WheelOnRumbleStripFrontRight',
 'WheelOnRumbleStripRearLeft',
 'WheelOnRumbleStripRearRight',
 'WheelInPuddleDepthFrontLeft',
 'WheelInPuddleDepthFrontRight',
 'WheelInPuddleDepthRearLeft',
 'WheelInPuddleDepthRearRight',
 'SurfaceRumbleFrontLeft',
 'SurfaceRumbleFrontRight',
 'SurfaceRumbleRearLeft',
 'SurfaceRumbleRearRight',
 'TireSlipAngleFrontLeft',
 'TireSlipAngleFrontRight',
 'TireSlipAngleRearLeft',
 'TireSlipAngleRearRight',
 'TireCombinedSlipFrontLeft',
 'TireCombinedSlipFrontRight',
 'TireCombinedSlipRearLeft',
 'TireCombinedSlipRearRight',
 'SuspensionTravelMetersFrontLeft',
 'SuspensionTravelMetersFrontRight',
 'SuspensionTravelMetersRearLeft',
 'SuspensionTravelMetersRearRight',
 'CarOrdinal',
 'CarClass',
 'CarPerformanceIndex',
 'DrivetrainType',
 'NumCylinders',
 'CarType',
 'ImpactX',
 'ImpactY',
 'PositionX',
 'PositionY',
 'PositionZ',
 'Speed',
 'Power',
 'Torque',
 'TireTempFrontLeft',
 'TireTempFrontRight',
 'TireTempRearLeft',
 'TireTempRearRight',
 'Boost',
 'Fuel',
 'DistanceTraveled',
 'BestLap',
 'LastLap',
 'CurrentLap',
 'CurrentRaceTime',
 'LapNumber',
 'RacePosition',
 'Accel',
 'Brake',
 'Clutch',
 'HandBrake',
 'Gear',
 'Steer',
 'NormalizedDrivingLine',
 'NormalizedAIBrakeDifference',
 'Unknown']

def GetParsedPacket(packet):
    vals = unpack(horizon_format, packet)
    return dict(zip(params, vals))